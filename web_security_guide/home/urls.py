from django.urls import path

from .views import home, signup

urlpatterns = [
    path('', home, name='home'),
    path('accounts/signup/', signup, name='signup'),
]