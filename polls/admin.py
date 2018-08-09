#-*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question

admin.site.register(Question)

''''
管理员可以编辑Question
增加其中内容
'''