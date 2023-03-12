from django.urls import path, include
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('Nposts/<int:pk>/', views.post_detail, name='post_detail'),
    path('Cposts/', views.create_post, name='create_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('posts/admin/', views.admin_post_list, name='admin_post_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('accounts/', include(('accounts.urls','accounts'), namespace= 'accounts')),
]
