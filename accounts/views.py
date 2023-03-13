from django.shortcuts import render, redirect
from blog.forms import  SignupForm
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})