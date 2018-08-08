from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    #这不仅仅能给你在命令行里使用带来方便，Django 自动生成的 admin 里也使用这个方法来表示对象。

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

'''每个变量代表数据库中的字段'''
"""每个字段通过 field 类表示一个实例， 比如 例如字符字段CharField和日期字段DateTimeField。 
这可以告诉Django，每个字段中保存着什么类型的数据。"""

"""比如 Field 实例的名字，比如 pub_date， question_txt ，机器可以读取，在python 中使用
其数值，并且数据库将其作为列名"""
"""可以给出人类可用名字，如question.pub_date, 有些会要求max_length, 可以给default"""


"""
激活：
1,加入setting
polls.apps.PollsConfig

2. 
python manage.py makemigrations polls
告诉django， 已经对模型进行变更，这一过程会有记录
    sqlmigrate命令接收迁移文件的名字并返回它们的SQL语句：
    python manage.py sqlmigrate polls 0001
    
    python manage.py check 检查问题，但不进行迁移
    
    直接使用 manage.py migrate
  
总的来说
    修改你的模型（在models.py文件中）。
    运行python manage.py makemigrations ，为这些修改创建迁移文件
    运行python manage.py migrate ，将这些改变更新到数据库中。
    这些改变可以参考 pools/migrations/0001_initial.py
原文
    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.



使用：
python manage.py shell
交互式界面,这样进入将会设置python的环境变量
We’re using this instead of simply typing “python”, because manage.py sets the 
DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your mysite/settings.py file.

使用2：
https://docs.djangoproject.com/en/1.11/intro/tutorial02/

from polls.models import Question, Choice

q.attribute
q.save()
"""

