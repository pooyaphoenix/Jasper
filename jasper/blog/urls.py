from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



pp_name='blog'
urlpatterns=[
    path('',views.index , name='index'),
    path('<int:book_id>/', views.detail , name= 'detail'),
    path('university/<int:uni_id>/', views.university_books, name='university_books'),
    path('field/<int:field_id>/', views.field_books, name='field_books'),

    path('register/', views.register, name='register'),
    path('jasper/', views.jasper , name = 'jasper'),
    path('myprofile/', views.myprofile , name = 'myprofile'),


    path('post/new/', views.post_new, name='post_new'),
    path('universitylist/', views.universitylist, name='universitylist'),
    path('filedlist/', views.fieldlist, name='fieldlist'),
    path('search/', views.search, name='search'),

    # path('list',views.BookListView.as_view(),name='book_list'),
   # path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    # bottom and above code are same !
    #re_path(r'^detail/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='book_detail'),

]

urlpatterns += staticfiles_urlpatterns()