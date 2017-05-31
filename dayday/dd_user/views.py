# coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from models import user_info
from hashlib import sha1

# Create your views here.


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
	user.user_post = uemail
	user.save()

	return redirect('/user/login/')

	

def name_exist(request):

	uname = request.GET.get('uname')
	count = user_info.objects.filter(user_name=uname).count()

	return JsonResponse({'count':count})


def login(request):



	return render(request, 'dayday/login.html')

# def index(request):
# 	dict = request.POST
# 	user_name = dict.get('username')
# 	user_passwd = dict.get('pwd')

# 	user_info.objects.

# 	context = {'user_name':username, 'user_passwd':user_passwd}




def user_center_info(request):
	return render(request, 'dayday/user_center_info.html')

def user_center_order(request):
	return render(request, 'dayday/user_center_order.html')

def user_center_site(request):
	return render(request, 'dayday/user_center_site.html')



