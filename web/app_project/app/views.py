from django.shortcuts import render, redirect

def index(request):
    '''Render main page'''
    return render(request, "app/index.html")
