from django.db import models

# What Defines a User
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=128)
	# liked_books = list of books a given user likes
	# books_uploaded = list of books uploaded by a given user
	create

class Book(models.Model):
	title = models.CharField(max_length=255)
	uploaded_by = models.ForeignKey(User, related_name='books_uploaded')
	users_who_like = models.ForeignKey(User, related_name='liked_books')
