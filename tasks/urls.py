from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.taskList, name='task-list'),
    path('tasksearch/', views.taskList, name='task-search'),
    path('<int:id>/', views.updateTask, name='update-task'),
    path('<int:id>/', views.taskView, name='task-view'),
    path('', views.taskList, name='list'),
]
