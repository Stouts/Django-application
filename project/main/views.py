""" Base views. """

from django.shortcuts import render


def index(request):
    """ Render simple page. """
    return render(request, 'main/base.html')


def profile(request):
    """ Render user profile page. """
    return render(request, 'main/base.html')
