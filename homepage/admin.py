from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExampleModel

admin.site.register(ExampleModel)
# admin.site.register(User, UserAdmin)li