from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ExampleModel

admin.site.register(ExampleModel)
# list_display = ("content","preview")
#
# def preview(self,obj):
#
#         return '<img src="/static/%s" height="64" width="64" />' %(obj.photo)
#
# preview.allow_tags = True
#
# preview.short_description = "picture"