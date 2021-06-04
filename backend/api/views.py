from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import *
from .models import *
import json, random, string
# Create your views here.

def randASCII(n):
	plain = ''

	for i in range(n):
		plain += random.choice(string.ascii_uppercase + string.digits)

	return plain

@csrf_exempt
def login(request):
	username = json.loads(request.body).get('username')
	password = json.loads(request.body).get('pass')
	try:
		this_user = User.objects.get(username=str(username))
		if check_password(password, str(this_user.password)):
			token = Token.objects.get(username=username).token
			return JsonResponse({'token': str(token), 'status': 200})
		else:
			return JsonResponse({'status': 500})
	except:
		return JsonResponse({'status': 502})

@csrf_exempt
def register(request):
	username = json.loads(request.body).get('username')
	password1 = json.loads(request.body).get('pass1')
	password2 = json.loads(request.body).get('pass2')

	# TODO: Add Security Feauture as Password length and ..
	try:
		User.objects.get(username=username)
		return JsonResponse({'status': 502})
	except:
		if username and password1 == password2:
			u = User(username=username)
			u.set_password(password2)
			u.save()
			token = Token(username=username, token=randASCII(200)).save()
			prof = Profile(username=username, name='', lastname='', email='', avatar='def').save()

			return JsonResponse({"status": 200})
		else:
			return JsonResponse({'status': 500})


@csrf_exempt
def getuser(request):
	token = json.loads(request.body).get('token')
	username = Token.objects.get(token=token).username
	user = Profile.objects.get(username=username)

	context = {
		'username': user.username,
		'name': user.name,
		'lname': user.lastname,
		'email': user.email,
		'avatar': user.avatar
	}

	return JsonResponse({'ID': context})

@csrf_exempt
def getposts(request):
	data = list(Post.objects.all().order_by('-publish').values())
	context = {
		'posts': data
	}

	return JsonResponse(context)

def post(request, slug):
	data = Post.objects.get(slug=slug)
	context= {
		'post': {
			'title': data.title,
			'thumbnail': data.thumbnail.url,
			'description': data.description,
			'body': data.body
		}
	}

	return JsonResponse(context)

@csrf_exempt
def edit(request):
	token = json.loads(request.body).get('token')
	name = json.loads(request.body).get('name')
	lname = json.loads(request.body).get('lname')
	email = json.loads(request.body).get('email')
	avatar = json.loads(request.body).get('avatar')

	user = Token.objects.get(token=token)

	UserProf = Profile.objects.get(username=user.username)
	UserProf.name = str(name)
	UserProf.lastname = str(lname)
	UserProf.email = str(email)
	UserProf.avatar = str(avatar)
	UserProf.save()
	

	return JsonResponse({'status': 200})