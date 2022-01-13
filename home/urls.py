from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("home/",views.index,name='home'),
    path("aboutus/",views.aboutus ,name="about_us"),
    path("contactus/",views.contactus,name="contact_us"),
    path('addblog/',views.addblog,name="addblog"),
    path("search/",views.search,name="search"),
    path("signup/",views.handlesignup,name="signup"),
    path("login/",views.handlelogin,name="signup"),
    path("logout/",views.handlelogout,name="signup"),

]
