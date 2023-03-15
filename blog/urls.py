from django.urls import path
from . import views
from .views import CustomLoginView, delete_user, delete_category

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('Nposts/<int:pk>/', views.post_detail, name='post_detail'),
    path('Cposts/', views.create_post, name='create_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('accounts/manage_users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('categories/<slug:slug>/delete/', delete_category, name='delete_category'),
    path('categories/', views.manage_slugs, name= "manage_slugs"),
    path('posts/<str:c_filter>/', views.post_list, name='filt_post_list'),
    path('<int:pk>/<int:pl>/delete_i/', views.delete_image, name='delete_image'),
]
