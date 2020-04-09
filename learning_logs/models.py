from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
	"""用户学习的主题模型"""
	text = models.CharField(max_length=200) 			  #由字符或文本组成的数据
	date_added = models.DateTimeField(auto_now_add=True)  #每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间。
	owner = models.ForeignKey(User)
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'entries'
	def __str__(self):
		"""返回模型的字符串表示"""	
		return self.text[:50] + "..."
"""		
class learning_log(models.Model):
	text = models.TextField(default='')
"""
	
	
	
