from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest  #导入单元测试模块
class NewVisitorTest(unittest.TestCase): 
	def setUp(self):           #在测试方法之前运行，打开浏览器
		self.browser = webdriver.Firefox()
	def tearDown(self): 	   #在测试方法之后运行，关闭浏览器
		self.browser.quit()
	
	def test_host(self): 
		self.browser.get('http://localhost:8000')
		self.assertIn('Learning Log', self.browser.title)
		"""张三最近发现了一个学习笔记网站，他访问主页后，发现了一个注册的链接文字，并点了进去"""
		link_text = self.browser.find_element_by_partial_link_text("Register an account").click()	
		"""张三认真的输入了自己帐号和密码"""
		inputbox = self.browser.find_element_by_id('id_username') 
		inputbox.send_keys('zhangsan') 
		inputbox.send_keys(Keys.ENTER) 
		passwd = "123456"
		inputbox = self.browser.find_element_by_id('id_password1') 
		inputbox.send_keys(passwd) 
		inputbox.send_keys(Keys.ENTER) 
		"""为了防止密码输错，他在下面验证密码框中，又输入了一次密码"""
		inputbox = self.browser.find_element_by_id('id_password2') 
		inputbox.send_keys(passwd) 
		inputbox.send_keys(Keys.ENTER) 

		register = self.browser.find_element_by_name('submit').click()
		if len(passwd)<=8:
			print("The password you set are all number")
		"""他发现自己的密码太短了，而且都是数字，没法注册...."""
		ul = self.browser.find_element_by_xpath('/html/body/div/div[2]/form/ul[3]')
		lis = ul.find_elements_by_xpath('li')
		print(len(lis))
		li_1 = self.browser.find_element_by_xpath('/html/body/div/div[2]/form/ul[3]/li[1]')
		if li_1:
			print(" The password you set does not meet the rules")
		"""张三太想使用这个网站学习了，于是他仔细想了一串密码后，再次输入一遍"""
		passwd = "123456yxyx"
		inputbox = self.browser.find_element_by_id('id_password1') 
		inputbox.send_keys(passwd) 
		inputbox.send_keys(Keys.ENTER) 
		"""为了防止密码输错，他在下面验证密码框中，又输入了一次密码"""
		inputbox = self.browser.find_element_by_id('id_password2') 
		inputbox.send_keys(passwd) 
		inputbox.send_keys(Keys.ENTER) 

		register = self.browser.find_element_by_name('submit').click()
		"""这次终于注册成功啦！"""
		print("you have register succcessfully!")
		#self.fail('Finish the test!')    #失败后返回指定的错误信息  
		
	
#使用这个语句检查自己是否在命令行中运行，而不是在其他脚本中导
if __name__ == '__main__':
	unittest.main(warnings='ignore')   #忽略抛出的异常
