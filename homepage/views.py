# -*-coding:utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from  django.http import HttpResponseForbidden
import datetime

from .forms import ImageUploadForm, SignUpForm, LoginForm
from .models import ExampleModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.views import generic
from .forms import NameForm


# class IndexView(generic.ListView):
#     template_name = 'homepage/homepage.html'
#
#     def get_queryset(self):
#         return 123
#
def index(request):
    today = 'image' + str(datetime.date.today())
    im = ExampleModel.objects.get(name="image2017-06-20")
    image = im.model_pic
    # return render(request, 'homepage/homepage.html')
    return render(request, 'homepage/homepage.html', {'image': image})

def to_login(request):
    return render(request, 'homepage/login.html')

def to_sign_up(request):
    return render(request,'homepage/sign up.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            return render(request, 'homepage/homepage.html', {'name': name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'homepage/homepage.html', {'name': form})


def hello(request):
    return render(request, 'homepage/hello.html')


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  # 有文件上传要传如两个字段
        if form.is_valid():
            image = form.cleaned_data['image']  # 直接在这里使用 字段名获取即可
            name = "image" + str(datetime.date.today())
            m = ExampleModel(model_pic=image, name=name)

            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User(username=username, password=password)
            user.save()
            return redirect('/')
            # return render(request, 'homepage/homepage.html')
    return HttpResponseForbidden('allowed only via POST')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(123)
                login(request, user)

                return redirect('/')
            else:
                url = request.POST.get('source_url')

                return HttpResponse("wrong user" + str(url))
            # password_exist = user_info.password
            # print(password_exist)
            # if password_exist == password_login:
            #     request.path = "/"
            #
            #     return render(request, 'homepage/homepage.html', {'username': username})
    return HttpResponseForbidden('allowed only via POST')

def personal_homepage(request):
    return render(request,'homepage/个人主页.html')