from django.shortcuts import render,redirect
from .models import Book,Universty,Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userform2 , PostForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.postgres.search import SearchVector


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
#def register(request):
      #if request.method == 'POST' :
            #form = UserForm(request.POST)
            #if form.is_valid():
             #     form.save()
              #    username = form.cleaned_data.get('username')
               #   messages.success(request , f'!ایجاد شد {username}  حساب کاربری')
                #  return redirect('index')
      #else:
       #     form = UserForm()

      


     # context = {
      #      'form' : form,
      #}
      #return render(request , 'accounts/register.html',context)


#صفحه ثبت نام 2
def register(request):
      if request.method == 'POST':
            form = userform2(request.POST)
            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')
                  messages.success(request , f'!ایجاد شد {username}  حساب کاربری')
                  return redirect('index')
      else:
            form = userform2()
      context = {
            'form' : form,
      }
      return render(request ,'accounts/register.html',context)



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def universitylist(request):
    allof_uni = Universty.objects.all()

    context = {
        'allof_uni': allof_uni
    }

    return render(request, 'blog/universiy_list.html',context)
def fieldlist(request):
    allof_filed = Field.objects.all()

    context = {
        'allof_filed': allof_filed
    }

    return render(request, 'blog/field_list.html',context)

def university_books(request, uni_id):
    allof_books = Book.objects.filter(university=uni_id)
    context = {
        'allof_books': allof_books,
    }
    return render(request, 'home.html', context)

def field_books(request, field_id):
    allof_books = Book.objects.filter(field=field_id)
    context = {
        'allof_books': allof_books,
    }
    return render(request, 'home.html', context)


#
# def search(request):
#     return HttpResponse(Book.objects.annotate(search=SearchVector('name', 'description', 'university'),).filter(search="جزوه"))

def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print (form.cleaned_data['my_form_field_name'])

            return HttpResponse('/thanks/') # Redirect after POST
    else:
        form = PostForm() # An unbound form

    return render('contact.html', {'form': form,})
#def post(self, request):
      #form = HomeForm(request.POST)
      #if form.is_valid():
            #text = form.cleaned_data['post']
            #form = HomeForm()
      #context = {
            #'form':form , 'text': text
      #}
      
      #return render(request, self.template_name , context)