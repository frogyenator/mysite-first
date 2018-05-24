from django.contrib import admin
#from django.db import models
# Register your models here.
from .models import User,ConfirmString

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','sex','email','c_time')

admin.site.register(User,UserAdmin)
admin.site.register(ConfirmString)