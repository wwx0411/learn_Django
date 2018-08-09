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


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def error(request):
    raise Http404

"""
每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404 。至于你还想干些什么，随便你。



"""