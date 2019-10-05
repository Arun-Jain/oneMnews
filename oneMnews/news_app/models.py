from django.db import models
from django.contrib.auth.models import (
		AbstractBaseUser, BaseUserManager
	)


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("Users must have a password")

		user_obj = self.model(email=self.normalize_email(email))
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, password=None):
		user = self.create_user(email, password=password, is_staff=True)
		return user

	def create_superuser(self, email, password=None):
		user = self.create_user(email, password=password, is_staff=True, is_admin=True)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'

	# REQUIRED_FIELD = [] #fullname

	objects = UserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_staff(self):
		"Is the user a admin member"
		return self.admin

	@property
	def is_active(self):
		"Is the user is active"
		return self.active

class NewsTypes(models.Model):
	news_type = models.CharField(max_length=50)

	class Meta:
		db_table = 'newstypes'

	def __str__(self):
		return "%s" % (self.news_type)

class Country(models.Model):
	country_name = models.CharField(max_length=120)

	class Meta:
		db_table = 'country'

	def __str__(self):
		return "%s" % (self.country_name)

class News(models.Model):
	TRENDING_CHOICE = (
			('Y', 'yes'),
			('N', 'no'),
		)
	# FLAG_CHOICE = (
	# 		('T', 'true'),
	# 		('F', 'false'),
	# 	)
	news_type = models.ForeignKey(NewsTypes, on_delete=models.CASCADE)
	heading = models.CharField(max_length=100)
	image_path = models.ImageField(upload_to='images', null=True, blank=True)
	news_body = models.TextField(max_length=600)
	is_trending = models.CharField(max_length=1, choices=TRENDING_CHOICE) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	flag = models.BooleanField(default=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

	class Meta:
		db_table = 'news'

	
