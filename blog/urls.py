from django.urls import path
from .views import (
	BlogListView, 
	BlogDetailView, 
	BlogCreateView,
	BlogUpdateView,
	BlogDeleteView)

urlpatterns = [
	path('blog/<int:pk>/delete' , BlogDeleteView.as_view() , name='blog_delete'),
	path('blog/<int:pk>/edit/' , BlogUpdateView.as_view() , name='blog_edit'),
	path('blog/new/' , BlogCreateView.as_view() , name='blog_new'),
	path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
	path('' , BlogListView.as_view() , name='home'),
]