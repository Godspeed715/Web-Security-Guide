from .views import videos
from django.urls import path

urlpatterns = [
    path('videos/<int:page_no>', videos, name='videos'),
]