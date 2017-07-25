from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Poll, Question, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'text', 'question', 'voters')
        read_only_fields = ('voters',)


class ChoiceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'text')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True,
                               source='choice_set',
                               read_only=True)

    class Meta:
        model = Question
        fields = ('url', 'text', 'poll', 'choices')


class QuestionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'text')


class PollSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True,
                                   source='question_set',
                                   read_only=True)
    description = serializers.CharField(max_length=1000,
                                        allow_blank=True)

    class Meta:
        model = Poll
        fields = (
            'url',
            'name',
            'description',
            'creator',
            'creation_date',
            'modification_date',
            'questions',
        )


class PollListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'is_superuser')

