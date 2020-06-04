from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError('Users must have an email address')
		if not password:
			raise ValueError('Users must have a password')

		user_obj = self.model(
			email=self.normalize_email(email)
		)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)

		return user_obj

	def create_staffuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True
		)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
			is_admin=True
		)
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

'''
class LoyaltyCard(models.Model):
	name = models.CharField(max_length=50)
	discount = models.FloatField()

	def __str__(self):
		return f'{self.name} Card'


class Profile(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	loyalty_card = models.ForeignKey(LoyaltyCard, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f'{self.user.email} Profile'

'''
