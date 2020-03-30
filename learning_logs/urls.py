from django.conf.urls import url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    
    # show all topics
    url(r'^topics/$', views.topics, name='topics'),
	# 特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
