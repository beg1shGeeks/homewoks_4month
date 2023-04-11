
from django.http import HttpResponse
from django.shortcuts import render
from . import models

def helloview(request):
    return HttpResponse('Hello World')

def bookview(request):
    book = models.Book.objects.all()
    context = {
        'book_object': book
    }
    return render(request, 'book.html', context)

