from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/index.html')


def base(request):
    return render(request,'home/base.html')

def course(request):
    return render(request,'home/course.html')

def about(request):
    return render(request,'home/about.html')