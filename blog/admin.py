from django.contrib import admin

from blog.models import Blogpost,Blogcomment

# Register your models here.
admin.site.register((Blogpost,Blogcomment))