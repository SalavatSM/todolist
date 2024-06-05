# tasks/urls.py
from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('tasks/', TaskListCreate.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task_detail'),

    path('tasks/new/', task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),

    path('api/tasks/', TaskListCreate.as_view(), name='task_list_create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task_detail'),
]




