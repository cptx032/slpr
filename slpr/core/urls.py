# coding: utf-8

from django.conf import settings
from django.conf.urls import url
from ratelimit.decorators import ratelimit

from core import views


def rate_limit(view):
    return ratelimit(key="ip", rate=settings.RATE_LIMIT_RATE, block=True)(view)


urlpatterns = [
    url(
        # license place recognitions
        r"^lprs/$",
        rate_limit(views.IndexAPIView.as_view()),
        name="api_mainview",
    ),
]
