from .views import owasp, owasp_list
from django.urls import path

urlpatterns = [
    path('', owasp_list, name='owasp_list'),
    path('<int:page_no>', owasp, name='owasp'),
]