# todo/urls.py
from django.urls import re_path
from . import views


#create로 호출하면, view에 있는 taskCreate를 view로써 보겠다.
urlpatterns = [
    re_path('create', views.TaskCreate.as_view(), name='create'),
    re_path('select', views.TaskSelect.as_view(), name='select'),
    re_path('toggle', views.TaskToggle.as_view(), name='toggle'),
    re_path('delete', views.TaskDelete.as_view(), name='delete'),
    re_path('',views.Todo.as_view(),name='todo'),

]