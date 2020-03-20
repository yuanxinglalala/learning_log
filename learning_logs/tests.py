from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from learning_logs.views import index
class HomePageTest(TestCase):
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/') 
		self.assertTemplateUsed(response, 'learning_logs/index.html') 
