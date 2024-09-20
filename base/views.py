from django.shortcuts import render,HttpResponse
from .models import *

def home(request):
     about_data = about.objects.first()  # Get the first entry in the About table
     resume_data = resume.objects.first()  # Get the first entry in the Resume table
     profile_image = profile_img.objects.first()  # Get the first profile image
     about_image = about_img.objects.first()
     context = {
        'about': about_data,
        'resume': resume_data,
        'profile_image': profile_image,
        'about_image': about_image,
     }
     data = about.objects.all()
     return render(request, 'home.html', context)

