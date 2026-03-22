from .views import videos
from django.urls import path

urlpatterns = [
    path('<int:page_no>', videos, name='videos'),
]