from django.db import models

# Create your models here.
class Contact(models.Model):
    
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    desc=models.TextField()
    def __str__(self):
            return self.name

class About(models.Model):
    email=models.CharField(max_length=150)
    comment=models.TextField()




