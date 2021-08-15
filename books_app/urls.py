from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index), # Our registration / login page
	path('login', views.login),
	path('logout', views.logout),
	path('register', views.register),
	path('books', views.books), # The main poge for the user, allows adding books - POST
	path('book/<int:id>', views.book_page), # The page for a book
	path('books/add', views.add_book),
	path('book/<int:id>/delete', views.delete_book),
	path('book/<int:id>/favorite', views.favorite),
	path('book/<int:id>/unfavorite', views.unfavorite),
	path('book/<int:id>/edit', views.edit),
]