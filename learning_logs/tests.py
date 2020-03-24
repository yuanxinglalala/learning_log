from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from learning_logs.views import index
from learning_logs.models import Item
class HomePageTest(TestCase):
	def test_index_page_returns_correct_html(self):
		response = self.client.get('/') 
		self.assertTemplateUsed(response, 'learning_logs/index.html') 
	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'learning_log_text': 'A new learning log item'}) #指定想发送的表单数据。
		self.assertIn('A new learning log item', response.content.decode())
		self.assertTemplateUsed(response, 'learning_logs/index.html')
		
class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) learning_log item'
		first_item.save()
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) learning_log item')
		self.assertEqual(second_saved_item.text, 'Item the second')
		
		
		
