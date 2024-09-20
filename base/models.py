from django.db import models

# Create your models here.
class about(models.Model):
     name = models.CharField(max_length=100)
     designation = models.CharField(max_length=100)
     about_me=models.TextField()
     def __str__(self):
          return self.name

class resume(models.Model):
     resume = models.FileField(upload_to='resume/media/profile_photo/')

class profile_img(models.Model):
     image = models.ImageField(upload_to='profile_photo/')
     
class about_img(models.Model):
     image = models.ImageField(upload_to='profile_photo/')

