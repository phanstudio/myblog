from django.shortcuts import render,  redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import datetime as dt
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'blog/edit_user.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def manage_accounts(request):
    users = User.objects.all()
    return render(request, 'blog/manage_accounts.html', {'users': users})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect(reverse('manage_users'))

def logout_view(request):
    logout(request)
    return redirect('blog:post_list')

class SessionIdleTimeout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time =  dt.now().strftime("%Y-%m-%d %H:%M:%S")#timezone.now()

        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')#
            if type(last_activity) == str:
                last_activity = dt.strptime(request.session.get('last_activity'), '%Y-%m-%d %H:%M:%S')
            if last_activity and (dt.strptime(current_time, '%Y-%m-%d %H:%M:%S') - last_activity).seconds > settings.SESSION_COOKIE_AGE:
                request.session.flush()
                return redirect('blog:login')

            request.session['last_activity'] = current_time#dt.strptime(current_time, '%Y-%m-%d %H:%M:%S')#current_time

        response = self.get_response(request)
        return response

def post_list(request):
    posts = Post.objects.all()
    is_admin = request.user.is_staff or request.user.is_superuser
    context = {
        'posts': posts,
        'is_admin': is_admin
    }
    return render(request, 'blog/post_list.html', context)

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    success_url = reverse_lazy('blog:post_list')

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.body = post.body.split("\n")
    return render(request, 'blog/post_detail.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})