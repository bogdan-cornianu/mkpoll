from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Poll,
    Question,
    Choice
)
from .serializers import (
    PollSerializer,
    PollListSerializer,
    QuestionSerializer,
    QuestionListSerializer,
    ChoiceSerializer,
    ChoiceListSerializer,
    UserSerializer,
)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (IsAuthenticated,)

    @detail_route(methods=['post'])
    def vote(self, request, pk=None):
        choice = self.get_object()
        question = choice.question
        voters = User.objects.filter(choice__question=question)
        if request.user in voters:
            return Response({'error': 'Cannot vote twice.'},
                            status=status.HTTP_400_BAD_REQUEST)
        choice.voters.add(request.user)
        return Response({'status': 'ok'})

    def get_serializer_class(self):
        if self.action == 'list':
            return ChoiceListSerializer
        return ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionListSerializer
        return QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return PollListSerializer
        return PollSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
