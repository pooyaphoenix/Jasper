from django.urls import path
from django.conf.urls import url
from . import views


pp_name='blog'
urlpatterns=[
    path('',views.index , name='index'),
    path('<int:book_id>/', views.detail , name= 'detail'),
    path('register/', views.register, name='register'),
    path('jasper/', views.jasper , name = 'jasper'),

   # path('list',views.BookListView.as_view(),name='book_list'),
   # path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    # bottom and above code are same !
    #re_path(r'^detail/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='book_detail'),

]