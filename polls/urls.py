#-*- coding: UTF-8 -*-
from django.conf.urls import url

from . import views

from . import views


'''
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/error
    url(r'^error$', views.error, name='error'),
]
'''


'''由于引用比较多时，可能产生重名现象，所以需要添加明明空间'''

# from django.conf.urls import url
#
# from . import views
#
# app_name = 'polls'
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#     url('<int:question_id>/vote/', views.vote, name='vote'),
#     url(r'^error$', views.error, name='error'),
# ]



'''
/polls/34
call:
 polls and then:
 detail(request=<HttpRequest object>, question_id='34')
 
    The question_id='34' part comes from (?P<question_id>[0-9]+).
    ?P<question_id> defines the name that will be used to identify the matched pattern  这里，question_id 与变量名相同
     [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).
'''




""""以下，采用django通用模板，简化代码量加快运行速度"""
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

""""
需要使用 pk ，不能使用choice_id

"""