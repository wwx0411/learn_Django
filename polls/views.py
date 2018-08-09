#coding:utf-8
from django.http import HttpResponse, Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
快捷填充，更加方便，功能和上列代码相同
'''

#
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', \n'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

"""

"""

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


from django.shortcuts import get_object_or_404, render


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''
快捷填充，更加方便，功能和上列代码相同
也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，
除了 get() 函数被换成了 filter() 函数。如果列表为空的话会抛出 Http404 异常。
'''




def error(request):
    raise Http404

"""
每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404 。至于你还想干些什么，随便你。



"""


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''
request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 
这里有<QueryDict: {u'csrfmiddlewaretoken': [u'u8jX8lJopTWpEFsp98B9cIhYR2c2LYlheqMIpWrvUCnTqVbEksy7xvkIlJ6pbABS'], u'choice': [u'4']}>
这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。

reverse() 函数。这个函数避免了我们在视图函数中hardcode URL
reverse('polls:results', args=(question.id,))='/polls/3/results/'
其中 3 是 question.id 的值。
重定向的 URL 将调用 'results' 视图来显示最终的页面

'''


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

""""以下由于django “generic views” system. 减少代码量，不再需要上面的代码"""
"""其中vote之后代码不变，"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # same as above, no changes needed.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''
我们在这里使用两个通用视图： ListView 和 DetailView
    1.结合model属性，能够判断哪里生效    
    2. url处要求使用pk值，不能再使用choice_id
    3.通用视图 DetailView/ListView 默认情况使用<app name>/<model name>_detail.html(<app name>/<model name>_list.html)
     即"polls/question_detail.html" 模板这里我们改变了    template_name = 'polls/results.html', 指定使用模板

在之前的教程中，提供模板文件时都带有一个包含 question 和 latest_question_list 变量的 context。
对于 DetailView ， question 变量会自动提供
    —— 因为我们使用 Django 的模型 (Question)， Django 能够为 context 变量决定一个合适的名字。
然而对于 ListView， 自动生成的 context 变量是 question_list。
    ——为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用 latest_question_list。
    作为一种替换方案，你可以改变你的模板来匹配新的 context 变量 
        —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。


'''


