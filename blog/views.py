
from django.contrib import messages,redirects
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Blogcomment, Blogpost
# Create your views here.
def bloghome(request):
    allposts=Blogpost.objects.order_by('-timeStamp')
    context={'posts':allposts}
    return render(request,'blog/bloghome.html',context)


def blogpost(request,slug):
    post=Blogpost.objects.filter(slug=slug).first()
    comment=Blogcomment.objects.filter(blogpost=post)
    context={'post':post,'comments':comment}
    return render(request,'blog/blogpost.html',context)



def postComment(request):
    if request.method=='POST':
        comment=request.POST["comment"]
        user=request.user
        postSno=request.POST["postSno"]
        blogpost=Blogpost.objects.get(sno=postSno)

        comment=Blogcomment(comment=comment,user=user,blogpost=blogpost)
        comment.save()      
      
        messages.success(request,"Your comment Has been Posted Successfully!")
        #return redirect("BHOME")
        return redirect(f"/blog/{blogpost.slug}")
    else:
        return render(request,'blog/blogpost.html')
