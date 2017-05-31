from django.db import models

# Create your models here.

class user_info(models.Model):
	user_name = models.CharField(max_length=20)
	user_passwd = models.CharField(max_length=40)
	user_email = models.CharField(max_length=20)
	user_tel = models.CharField(max_length=20, default='')
	user_post = models.CharField(max_length=20, default='')
	user_addr = models.CharField(max_length=255, default='')

	class Meta:
		db_table = 'user_info'


