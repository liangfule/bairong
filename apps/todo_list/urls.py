from django.urls import path
from . import views

urlpatterns = [
    #测试
    path('test_function/', views.test_function),
    path('todo_task_list/', views.todo_task_list),
    path('single_person_todo/', views.single_person_todo)

]