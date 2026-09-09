from django.urls import path
from .views import home
# from .views import home, signup                             # --- AUTH (commented out) ---

urlpatterns = [
    path('', home, name='home'),
    # path('accounts/signup/', signup, name='signup'),        # --- AUTH (commented out) ---
]
