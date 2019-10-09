from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})', views.BookDetailView.as_view(), name='book-detail'),
    url(r'authors/', views.AuthorListView.as_view(), name='authors'),
    url(r'author/(?P<pk>[0-9]+)/$',
         views.AuthorDetailView.as_view(), name='author-detail'),
]