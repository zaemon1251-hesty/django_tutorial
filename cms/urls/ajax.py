from django.urls import path
import os
import sys

try:
    from cms.views import render_markdown, check
except BaseException:
    raise


urlpatterns = [
    path(
        '',
        check
    ),
    path(
        'render',
        render_markdown
    ),
]
