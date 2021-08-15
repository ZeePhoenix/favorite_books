from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt

# Our main Login and Registration Page
def index(request):
	return render(request, "register_page.html")

def register(request):
	errors = User.objects.user_validatior(request.POST)
	if len(errors) > 0:
		for key, val in errors.items():
			messages.error(request, val)
			return redirect("/")
	else:
		password = request.POST['password']
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		print(pw_hash)
		user = User.objects.create(
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			password = pw_hash)
		request.session['userid'] = user.id
		return redirect("/books")

def login(request):
	user = User.objects.filter(email=request.POST['email'])
	if user:
		logged_user = user[0]
		if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
			request.session['userid'] = logged_user.id
			print("Logged into the Mainframe")
			return redirect("/books")
	return redirect('/')

def books(request):
	try:
		user = User.objects.filter(id=request.session['userid'])
	except:
		return redirect("/")
		
	context = { 'user' : user[0] }
	return render(request, "books.html", context)

def book_page(request, id):
	try:
		user = User.objects.filter(id=request.session['userid'])
		book = Book.objects.filter(id=id)
	except:
		print("Error finding user and/or book")
	context = { 'user': user, 'book': book , 'all_books' : Book}
	return render(request, "book_page.html", context)

def add_book(request):
	errors = User.objects.book_validator(request.POST)
	if len(errors) > 0:
		for key, val in errors.items():
			messages.error(request, val)
			return redirect("/")
	else:
		book = Book.objects.create(
			title = request.POST['title'],
			description = request.POST['description'])
		user = User.objects.get(id=request.session['userid'])
		user.liked_books.add(book)
		return redirect("/book/%d"%book.id)
	return

def delete_book(request, id):
	book = Book.objects.get(id=id)
	book.delete()
	return redirect(request.meta['HTTP_REFERER'])

def favorite(request, id):
	user = User.objects.get(id=request.session['userid'])
	user.liked_books.add(Book.objects.get(id=id))
	return redirect(request.meta['HTTP_REFERER'])

def logout(request):
	request.session.clear()
	return redirect("/")