from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('get/', views.get_users),
    path('create/', views.create_user),
    path('update/<int:user_id>/', views.update_user),
    path('delete/<int:user_id>/', views.delete_user),
    path('login/', views.login_view),
    path('login/checksession', views.check_session_view),
    path('logout/<int:session_id>/', views.logout_view),
]
