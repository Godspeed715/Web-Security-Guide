# home/views.py
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm      # --- AUTH (commented out) ---


# Create your views here.
def home(request):
    return render(request, 'home.html')


# def signup(request):                                        # --- AUTH (commented out) ---
#     if request.method == 'POST':                            # --- AUTH (commented out) ---
#         form = UserCreationForm(request.POST)               # --- AUTH (commented out) ---
#         if form.is_valid():                                 # --- AUTH (commented out) ---
#             form.save()                                     # --- AUTH (commented out) ---
#             redirect('home')                                # --- AUTH (commented out) ---
#     else:                                                   # --- AUTH (commented out) ---
#         form = UserCreationForm()                           # --- AUTH (commented out) ---
#     return render(request, 'signup.html', {'form': form})  # --- AUTH (commented out) ---
