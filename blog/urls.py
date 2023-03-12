from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('Nposts/<int:pk>/', views.post_detail, name='post_detail'),
    path('Cposts/', views.create_post, name='create_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
