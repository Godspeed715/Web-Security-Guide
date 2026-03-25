from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})