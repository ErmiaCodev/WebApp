from django.urls import path
from .views import * 
urlpatterns = [
	path('login/', login),
	path('register/', register),
	path('getuser/', getuser),
	path('posts/', getposts),
	path('post/<slug>', post),
	path('edituser/', edit)
]