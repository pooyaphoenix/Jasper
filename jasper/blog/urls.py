from django.urls import path,re_path
from . import views

pp_name='blog'
urlpatterns=[
    path('',views.index , name='index'),
    path('<int:book_id>/', views.detail , name= 'detail'),

   # path('list',views.BookListView.as_view(),name='book_list'),
   # path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    # bottom and above code are same !
    #re_path(r'^detail/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='book_detail'),

]