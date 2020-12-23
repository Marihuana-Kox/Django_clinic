from django.urls import path

from . views import IndexRecorderView

urlpatterns = [
    path('records/', IndexRecorderView.as_view(), name='record-views'),
]