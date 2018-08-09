from django.conf.urls import url

from . import views

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
/polls/34
call:
 polls and then:
 detail(request=<HttpRequest object>, question_id='34')
 
    The question_id='34' part comes from (?P<question_id>[0-9]+).
    ?P<question_id> defines the name that will be used to identify the matched pattern  这里，question_id 与变量名相同
     [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).
'''