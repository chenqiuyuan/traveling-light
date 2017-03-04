from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import generic


# class IndexView(generic.ListView):
    # template_name = 'homepage/index.html'

from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
