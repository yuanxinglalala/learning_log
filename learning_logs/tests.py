from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from learning_logs.views import index
class HomePageTest(TestCase):
	def test_index_page_returns_correct_html(self):
		response = self.client.get('/') 
		self.assertTemplateUsed(response, 'learning_logs/index.html') 
	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'learning_log_text': 'A new learning log item'}) #指定想发送的表单数据。
		self.assertIn('A new learning log item', response.content.decode())
		self.assertTemplateUsed(response, 'learning_logs/index.html')
