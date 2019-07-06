from django.shortcuts import render,redirect
from .models import Book,Universty,Field, profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm , PostForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def index(request):

      context = {
            'allof_books' : Book.objects.all()
      }

      return render(request , 'home.html',context )



#نمایش کتاب ها با list view
#class base view
class PostListView(ListView):
      model = Book
      template_name = 'home.html' #refrence: <app>/<mode>_<viewType>.html
      context_object_name = 'allof_books'
      ordering = ['-date_posted']



#نمایش جزئیات پست ها با استفاده از detail view
#class base view
class PostDetailView(DetailView):
      model = Book



#ثبت آگهی با استفاده از create view
#class base view
class PostCreatelView(LoginRequiredMixin, CreateView):
      model = Book
      fields = ['name', 'master','field','university','status','status2','price','description']
      success_url = '/'
      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)




#ّبروزرسانی آگهی با استفاده از update view
#class base view
class PostUpdatelView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model = Book
      fields = ['name', 'master','field','university','status','status2','price','description']
      success_url = '/'

      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

      def test_func(self):
            book = self.get_object()
            if self.request.user == book.user:
                  return True
            return False




#حذف پست ها با استفاده از delete view
#class base view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
      model = Book
      success_url = '/'
      
      def test_func(self):
            book = self.get_object()
            if self.request.user == book.user:
                  return True
            return False







def detail(request,book_id):
      bookdetail = Book.objects.get(pk = book_id)
      context = {
            'bookdetail' : bookdetail,
      }
      return render (request , 'detail.html',context)

def jasper(request):
      return render(request,'jasper.html')



#صفحه ثبت نام 2
def register(request):
      if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')
                  messages.success(request , f'!ایجاد شد {username}  حساب کاربری')
                  return redirect('/login')
      else:
            form = UserForm()
      context = {
            'form' : form,
      }
      return render(request ,'accounts/register.html',context)




#پروفایل کاربری
@login_required
def myprofile(request):
      if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
            request.FILES, 
            instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                  u_form.save()
                  p_form.save()
                  messages.success(request, f'حساب کاربری با موفقیت بروز رسانی شد.')
                  return redirect('myprofile')
      else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

      context = {
            'u_form' : u_form,
            'p_form' : p_form
      }
      return render(request, 'accounts/profile.html', context)




#ثبت آگهی
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            Book.user = User
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




#لیست دانشگاه ها
def universitylist(request):
    allof_uni = Universty.objects.all()

    context = {
        'allof_uni': allof_uni
    }

    return render(request, 'blog/universiy_list.html',context)




#لیست رشته ها
def fieldlist(request):
    allof_filed = Field.objects.all()

    context = {
        'allof_filed': allof_filed
    }

    return render(request, 'blog/field_list.html',context)



#جزوه های موجود در دانشگاه مورد نظر
def university_books(request, uni_id):
    allof_books = Book.objects.filter(university=uni_id)
    context = {
        'allof_books': allof_books,
    }
    return render(request, 'home.html', context)



#جزوه های موجود در رشته ی مورد نظر
def field_books(request, field_id):
    allof_books = Book.objects.filter(field=field_id)
    context = {
        'allof_books': allof_books,
    }
    return render(request, 'home.html', context)



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





