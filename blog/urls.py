from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [

    path('',views.bloghome,name="BHOME"),
    path('blog/',views.bloghome,name="BHOME"),
    path('postComment/',views.postComment,name="postcomment"),
    path('<str:slug>',views.blogpost,name='blogpost'),
    
    
    
  
   
]