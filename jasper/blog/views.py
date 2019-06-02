from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm
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

def jasper(request):
      return render(request,'jasper.html')

#صفحه ی ثبت نام
def register(request):
      if request.method == 'POST' :
            form = UserForm(request.POST)
            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')
                  messages.success(request , f'!ایجاد شد {username}  حساب کاربری')
                  return redirect('index')
      else:
            form = UserForm()

      


      context = {
            'form' : form,
      }
      return render(request , 'accounts/register.html',context)









#def post(self, request):
      #form = HomeForm(request.POST)
      #if form.is_valid():
            #text = form.cleaned_data['post']
            #form = HomeForm()
      #context = {
            #'form':form , 'text': text
      #}
      
      #return render(request, self.template_name , context)