from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('Nposts/<int:pk>/', views.post_detail, name='post_detail'),
    path('Cposts/', views.create_post, name='create_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('posts/admin/', views.admin_post_list, name='admin_post_list'),
]
