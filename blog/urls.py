from django.urls import path
from .views import BlogListView , BlogDetailView , BlogCreateView

urlpatterns = [
	path('blog/new/' , BlogCreateView.as_view() , name='blog_new'),
	path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
	path('' , BlogListView.as_view() , name='home'),
]