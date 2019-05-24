from .models import Blog
from django.views.generic import ListView , DetailView


class BlogListView(ListView):
	model = Blog
	template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blog_detail.html'