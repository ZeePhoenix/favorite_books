from django.db import models
import re

# Methods our User class needs
class Manager(models.Manager):
	def user_validatior(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData["first_name"]) < 2 or not str.isalpha(postData["first_name"]):
			errors['first_name'] = ("Invalid First Name")
		if len(postData["last_name"]) < 2 or not str.isalpha(postData["last_name"]):
			errors['last_name'] = ("Invalid Last Name")
		if not EMAIL_REGEX.match(postData["email"]):
			errors['email'] = ("Invalid Email Address")
		if len(User.objects.filter(email=postData['email'])) > 0:
			errors['email'] = ("Email alread in use")
		if len(postData['password']) < 8:
			errors['password'] = ("Password not long enough")
		if not postData['password'] == postData['password_confirm']:
			errors['password_confirm'] = ("Passwords do not match")
		return errors
	def book_validator(self, postData):
		errors = {}
		if len(postData['title']) < 1:
			errors['title'] = ("Book must have a title")
		if len(postData['description']) < 5:
			errors['description'] = ("Description must be at least 5 characters")
		return errors

# What Defines a User
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=128)
	# liked_books = list of books a given user likes
	# books_uploaded = list of books uploaded by a given user
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Manager()

# What defines a Book
class Book(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)
	users_who_like = models.ForeignKey(User, related_name='liked_books', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Manager()