from django.shortcuts import render

def index(request):
    return render(request, 'book/index.html')

def add(request):
    return render(request, 'book/add.html')