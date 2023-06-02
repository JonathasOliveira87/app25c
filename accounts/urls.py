from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.registration, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile_user, name='profile_user'),
    path('happyday/', views.happy_day, name='happy_day'),

]
