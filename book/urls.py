from django.urls import path
from book.views import helloview, bookview

urlpatterns = [
    path('hello/', helloview, name='hello'),
    path('book/', bookview, name='book'),
]