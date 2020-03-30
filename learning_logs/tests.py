from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from learning_logs.views import index
from learning_logs.views import topics
from learning_logs.models import Topic
class HomePageTest(TestCase):
	def test_index_page_returns_correct_html(self):
		response = self.client.get('/') 
		self.assertTemplateUsed(response, 'learning_logs/topics.html') 
	'''
	def test_can_save_a_POST_request(self):
		self.client.post('/', data={'learning_log_text': 'A new learning log item'}) #指定想发送的表单数据。
		self.assertEqual(learning_log.objects.count(), 1)
		new_item = learning_log.objects.first()
		self.assertEqual(new_item.text, 'A new learning log item')
		
	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'learning_log_text': 'A new learning log item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')
	def test_displays_all_list_items(self):
		learning_log.objects.create(text='itemey 1')
		learning_log.objects.create(text='itemey 2')
		
		response = self.client.get('/')
		
		self.assertIn('itemey 1', response.content.decode())
		self.assertIn('itemey 2', response.content.decode())
		
class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = learning_log()
		first_item.text = 'The first (ever) learning_log item'
		first_item.save()
		second_item = learning_log()
		second_item.text = 'Item the second'
		second_item.save()
		saved_items = learning_log.objects.all()
		self.assertEqual(saved_items.count(), 2)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) learning_log item')
		self.assertEqual(second_saved_item.text, 'Item the second')
'''
		
		
		
