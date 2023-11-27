from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def delivery(request):
    """ A view to return the delivery page"""
    return render(request, "home/delivery.html")


def about_us(request):
    """ A view to return the about us page"""
    return render(request, 'home/about_us.html')


def returns(request):
    """ A view to return the returns page"""
    return render(request, "home/returns.html")


def privacy_policy(request):
    """ A view to return the privacy_policy page"""
    return render(request, "home/privacy_policy.html")
