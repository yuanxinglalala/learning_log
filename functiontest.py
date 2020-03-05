from selenium import webdriver
import unittest  #导入单元测试模块
class NewVisitorTest(unittest.TestCase): 
	def setUp(self):           #在测试方法之前运行，打开浏览器
		self.browser = webdriver.Firefox()
	def tearDown(self): 	   #在测试方法之后运行，关闭浏览器
		self.browser.quit()
	def test_to_do(self): 
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do', self.browser.title) 
		self.fail('Finish the test!')    #失败后返回指定的错误信息  

#使用这个语句检查自己是否在命令行中运行，而不是在其他脚本中导
if __name__ == '__main__':
	unittest.main(warnings='ignore')   #忽略抛出的异常
