from .views import owasp
from django.urls import path

urlpatterns = [
    path('owasp/<int:page_no>', owasp, name='owasp'),
]