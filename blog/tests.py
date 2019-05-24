from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Blog

class BlogTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
				username='testuser',
				email='test@email.com',
				password='secret'
			)
		self.blog = Blog.objects.create(
			title='blog title',
			body='blog body',
			author=self.user
			)

	def test_string_representation(self):
		blog = Blog(title='TITLE')
		self.assertEqual(str(blog) , blog.title)
		self.assertEqual(str(blog) , 'TITLE') # added extra

	def test_blog_content(self):
		self.assertEqual(f'{self.blog.title}' , 'blog title')
		self.assertEqual(f'{self.blog.body}' , 'blog body')
		self.assertEqual(f'{self.blog.author}' , 'testuser')

	def test_blog_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code , 200)
		self.assertContains(response , 'blog body')
		self.assertContains(response , 'blog title') # added extra
		self.assertTemplateUsed(response , 'home.html')

	def test_blog_detail_view(self):
		response = self.client.get('/blog/1/')
		no_response = self.client.get('/blog/1000000/')
		response_ = self.client.get(reverse('blog_detail' , args=['1'])) # added extra
		self.assertEqual(response.status_code , response_.status_code)
		self.assertEqual(response.status_code , 200)
		self.assertEqual(no_response.status_code , 404)
		self.assertContains(response , 'blog title')
		self.assertTemplateUsed(response , 'blog_detail.html')

	def test_get_absolute_url(self):
		self.assertEqual(self.blog.get_absolute_url() , 'blog/1/')

	def test_blog_create_view(self):
		response = self.client.post(reverse('blog_new'), {
			'title': 'New title',
			'body': 'New text',
			'author': self.user})
		self.assertEqual(response.status_code , 200)
		self.assertContains(response , 'New title')
		self.assertContains(response , 'New text')

	def test_blog_update_view(self):
		response = self.client.post(reverse('blog_edit', args='1'), {
		'title': 'Updated title',
		'body': 'Updated text'})
		self.assertEqual(response.status_code, 302)

	def test_blog_delete_view(self):
		response = self.client.get(
		reverse('blog_delete', args='1'))
		self.assertEqual(response.status_code, 200)