from django.urls import path
from .views import task_list, add_task, complete_task, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),  
    path('add/', add_task, name='add_task'), 
    path('task/<int:task_id>/complete/', complete_task, name='complete_task'), 
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),  
]
