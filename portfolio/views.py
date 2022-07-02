from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html', {})


def portfoliodetail(request):
    return render(request, 'portfolio/portfolio-details.html', {})

def postDetails(request, pk):

    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'portfolio/post_details.html', context)

def blog(request):

    posts = Post.objects.all()

    context = {

        'posts': posts

    }
    return render(request, 'portfolio/blog.html', context)


def contact(request):

    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail( 
                name, 
                message, 
                settings.EMAIL_HOST_USER, 
                ['babati02@yahoo.com'], 
                fail_silently= False
                )
        return redirect('index')

    else:   
        return render(request, 'portfolio/contact.html', {})