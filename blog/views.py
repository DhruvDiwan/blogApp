from .models import Blog
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView

class BlogListView(ListView):
	model = Blog
	template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
	model = Blog
	template_name = 'blog_new.html'
	fields = '__all__'