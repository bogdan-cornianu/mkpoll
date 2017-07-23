"""
"""
# pylint: disable=invalid-name
from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    PollViewSet,
    QuestionViewSet,
    ChoiceViewSet,
    UserViewSet,
)


router = routers.DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url('^', include(router.urls))
]
