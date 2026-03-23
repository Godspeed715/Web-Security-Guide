from .views import videos, videos_list
from django.urls import path

urlpatterns = [
    path('', videos_list, name='videos_list'),
    path('<int:page_no>', videos, name='videos'),
]