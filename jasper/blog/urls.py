from django.urls import path
from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreatelView, PostUpdatelView, PostDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



pp_name='blog'
urlpatterns=[
    path('', PostListView.as_view() , name='index'),
    path('post/<int:pk>/',PostDetailView.as_view() , name= 'detail'),
    path('post/<int:pk>/update/',PostUpdatelView.as_view() , name= 'update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name= 'delete'),
    path('university/<int:uni_id>/', views.university_books, name='university_books'),
    path('field/<int:field_id>/', views.field_books, name='field_books'),

    path('register/', views.register, name='register'),
    path('jasper/', views.jasper , name = 'jasper'),
    path('myprofile/', views.myprofile , name = 'myprofile'),


    path('post/new/', PostCreatelView.as_view(), name='post_new'),
    path('universitylist/', views.universitylist, name='universitylist'),
    path('filedlist/', views.fieldlist, name='fieldlist'),
    path('search/', views.search, name='search'),

    # path('list',views.BookListView.as_view(),name='book_list'),
   # path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    # bottom and above code are same !
    #re_path(r'^detail/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='book_detail'),

]

urlpatterns += staticfiles_urlpatterns()