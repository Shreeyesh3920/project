
# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from blog.models import Blogpost
from .models import Contact,About

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
    return redirect('/blog')

def addblog(request):
    return render(request,"blog/addblog.html")

def aboutus(request):
    if request.method=='POST':
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        if email=='' or comment=='':
            messages.warning(request,"Fill information correctly!")
            return redirect("BHOME")
        else:
            about=About(email=email,comment=comment)
            about.save()
            messages.success(request,"Message send Successfully!")
            return redirect("BHOME")
    else:
        return render(request,'home/about.html')

def contactus(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        if name=='' or email=='' or desc=='':
            messages.warning(request,"Fill information correctly!")
            return redirect("BHOME")   
        else:
            contact= Contact(name=name,email=email,desc=desc)
            contact.save()
            messages.success(request,"Message send Successfully!")
            return redirect("BHOME")
            
            
    else:
        return render(request,'home/contact.html')

def search(request):
    query=request.GET.get("query")
    if len(query)>78:
        post=[]
    else:
        posttitle=Blogpost.objects.filter(title__icontains=query)
        postcontent=Blogpost.objects.filter(content__icontains=query)
        postauthor=Blogpost.objects.filter(author__icontains=query)
        
        post=posttitle.union(postcontent,postauthor)
    params={'posts':post,'querys':query}
    return render(request,"home/search.html",params)


def handlesignup(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if username=='' or email=='' or pass1=='' or pass2=='':
            messages.warning(request,"Fill the related Information correctly")
            return redirect("BHOME")
        else:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request,"Your DIGITAL OCEAN account has been Successfully created")
            return redirect("BHOME")
        
    else:
        return render(request,"home/index.html")

    
def handlelogin(request):
    if request.method=="POST":
        login_username=request.POST["login_username"]
        login_pass=request.POST["login_pass"]
        user=authenticate(username=login_username,password=login_pass)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Successfully!")
            return redirect("BHOME")
    else:
        messages.warning(request,"Not Found!")
        return render(request,"home/index.html")


def handlelogout(request):
        logout(request)
        messages.success(request,"Successfully Logged Out")
        return redirect("BHOME")

def addblog(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        slug=request.POST.get('slug')
        if  title=='' or content=='' or author==''  or slug=='':
            messages.success(request,"Blog Uploaded Successfully!")
            return redirect("BHOME")
        else:
            blog=Blogpost(title=title,content=content,author=author,slug=slug)
            blog.save()
            messages.success(request,"Blog Uploaded Successfully!")
            return render(request,"blog/addblog.html") 
    else:
        return render(request,"blog/addblog.html")



