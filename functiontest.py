from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest  #导入单元测试模块
class NewVisitorTest(unittest.TestCase): 
	def setUp(self):           #在测试方法之前运行，打开浏览器
		self.browser = webdriver.Firefox()
	def tearDown(self): 	   #在测试方法之后运行，关闭浏览器
		self.browser.quit()
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_learning_log_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
	def test_can_start_a_list_and_retrieve_it_later(self): 
		self.browser.get('http://localhost:8000')
		self.assertIn('Leaning ', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('leaning ', header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_learning_log') 
		self.assertEqual(inputbox.get_attribute('placeholder'),
				'Enter a learning log')
		inputbox.send_keys('I learned Chess Today') 
		inputbox.send_keys(Keys.ENTER) 
		time.sleep(1) 
		self.check_for_row_in_list_table('1:I learned Chess Today')
		
		inputbox = self.browser.find_element_by_id('id_new_learning_log') 
		inputbox.send_keys('I learned Climbing Today') 
		inputbox.send_keys(Keys.ENTER) 
		time.sleep(1) 
		
		self.check_for_row_in_list_table('1:I learned Chess Today')
		self.check_for_row_in_list_table('2:I learned Climbing Today')
		
		table = self.browser.find_element_by_id('id_learning_log_table')
		rows = table.find_elements_by_tag_name('tr') 
		#self.assertTrue(
		self.assertIn('1:I learned Chess Today', [row.text for row in rows])
		
		self.fail('Finish the test!')    #失败后返回指定的错误信息  
		
		

#使用这个语句检查自己是否在命令行中运行，而不是在其他脚本中导
if __name__ == '__main__':
	unittest.main(warnings='ignore')   #忽略抛出的异常
