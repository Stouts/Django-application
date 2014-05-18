""" Base views. """

from django.shortcuts import render


def index(request):
    """ Render simple page. """
    return render(request, 'base.html')
