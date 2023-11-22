from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def delivery(request):
    """ A view to return the index page and products"""
    return render(request, "home/delivery.html")

def about_us(request):
    return render(request, 'home/about_us.html')      