from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def home(request):
    return HttpResponse('<h1>Главная</h1>')


def about(request):
    return HttpResponse('<h1>Наш клуб</h1>')


def lists(request):
    names = ['Igor', 'Denis', 'Roma']
    render(request, 'blockchainWebService/index.html',  context={'names': names})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Неверный URL!</h1>')
