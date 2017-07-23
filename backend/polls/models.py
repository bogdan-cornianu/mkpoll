from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    creator = models.ForeignKey(User,
                                null=True,
                                on_delete=models.SET_NULL)
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Poll: {self.name}'


class Question(models.Model):
    text = models.CharField(max_length=500)
    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'Question: {self.text}'


class Choice(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    voters = models.ManyToManyField(User,
                                    verbose_name='list of voters')

    def __str__(self):
        return f'Choice: {self.text}'
