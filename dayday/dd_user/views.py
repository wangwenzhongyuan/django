# coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from models import user_info
from hashlib import sha1

# Create your views here.

def index(request):
	return render(request,'dayday/index.html')


def register(request):
	context = {'title':'天天生鲜-注册'}

	return render(request, 'dayday/register.html', context)


def register_handle(request):

	dict = request.POST

	uname = dict.get('user_name')

	result = user_info.objects.filter(user_name=uname)

	upwd = dict.get('pwd')
	uemail = dict.get('email')
	uallow = dict.get('allow')
	
	s1 = sha1()
	s1.update(upwd)
	newpwd = s1.hexdigest()


	
	user = user_info()
	user.user_name = uname
	user.user_passwd = newpwd
	user.user_email = uemail
	user.save()

	return redirect('/user/login/')

	

def name_exist(request):

	uname = request.GET.get('uname')
	count = user_info.objects.filter(user_name=uname).count()

	return JsonResponse({'count':count})


def login(request):
	#当请求到登陆页面时,默认姓名和密码都是正确的,0
	uname = request.COOKIES.get('uname', '')
	context = {'title':'天天生鲜-登录', 'err_name':0, 'err_passwd':0, 'uname':uname}

	return render(request, 'dayday/login.html', context)

def login_handle(request):
	dict = request.POST
	uname = dict.get('username')
	upasswd = dict.get('pwd')
	# 勾选了记住密码,会读取到设置的value值,否则是0
	rem = dict.get('rem',0)
	user = user_info.objects.filter(user_name=uname)
	if len(user) >= 1:
		print user[0].user_name
		# 把读取的密码加密,用来跟数据库的信息进行比较
		s1 = sha1()
		s1.update(upasswd)
		wpwd = s1.hexdigest()

		rpwd = user[0].user_passwd
		if rpwd == wpwd:
			# 当用户名和密码都正确时候,页面会跳转到主页,
			# 如果cookie中有访问地址,则获取地址,没有的话为'/'
			# 这个url是在其他页面写入的

			url = request.COOKIES.get('url', '/')

			# 构造redirect对象
			re = HttpResponseRedirect(url)
			# 吧cookie信息设置为空,并且立即过期

			re.set_cookie('url', '', max_age=-1)

			#判断是否勾选记住用户名
			if rem == 1:
				re.set_cookie('uname',uname)

			else:
				re.set_cookie('uname', '', max_age=-1)

			# 成功了，吧用户名写入session。这样在其他页面会把用户信息显示出来
            # 存id是为了方便查询
			request.session['uname_id'] = user[0].id
			request.session['uname'] = uname

			return re

		else:
			#密码错误,此时应该还是返回在登陆页,同时如果想让html页面提示密码错误,需要
			# 传过去一个标志,所以可以构造一个上下文
			context = {'title':'天天生鲜-登录', 'err_name':0, 'err_passwd':1, 'uname':uname, 'upasswd':upasswd }
			return render(request,'dayday/login.html', context)
	else:

		context = {'title':'天天生鲜-登录', 'err_name':1, 'err_passwd':0, 'uname':uname, 'upasswd':upasswd }
	return render(request,'dayday/login.html', context)




def user_center_info(request):
	uname = request.session['uname']
	uid = request.session['uname_id']
	utel = user_info.objects.get(id=uid).user_tel
	uaddr = user_info.objects.get(id=uid).user_addr

	context = {'uname':uname, 'uid':uid,'uaddr':uaddr}


	return render(request, 'dayday/user_center_info.html', context)

def user_center_order(request):





	return render(request, 'dayday/user_center_order.html')

def user_center_site(request):

	# uname = request.session['uname']
	# print uname
	uid = request.session['uname_id']
	user = user_info.objects.get(id=uid)
	print user

	# uid = request.session['uname_id']
	# utel = user_info.objects.get(id=uid).user_tel
	# uaddr = user_info.objects.get(id=uid).user_addr

	
	# 判断如果进行表单提交了,便对数据库存储的信息进行更改
	if request.method == 'POST':

		dic = request.POST
		# uname.user_name = dic.get('uname')
		user.user_addr = dic.get('uaddr')
		user.user_tel = dic.get('utel')
		user.user_post = dic.get('upost')
		user.save()

	context = {'uname':user}

	return render(request, 'dayday/user_center_site.html', context)



