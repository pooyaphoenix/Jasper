from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):

      allof_books = Book.objects.all()

      context = {
            'allof_books' : allof_books
      }

      return render(request , 'home.html',context )

def detail(request,book_id):


      bookdetail = Book.objects.get(pk = book_id)
      context = {
            'bookdetail' : bookdetail,
      }
      return render (request , 'detail.html',context)


