from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Blogpost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=RichTextField()
    author=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    timeStamp=models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return self.title

class Blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blogpost=models.ForeignKey(Blogpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
            return self.user.username