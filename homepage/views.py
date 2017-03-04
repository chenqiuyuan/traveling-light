# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'homepage/homepage.html'

    def get_queryset(self):
        return 123
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def hello(request):
    return render(request, 'homepage/hello.html')