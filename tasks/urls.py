from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newGroup', views.newGroup, name='newGroup'),
    url(r'^(?P<group_id>[0-9]+)/newTask', views.newTask, name='newTask'),
    url(r'^(?P<group_id>[0-9]+)/(?P<task_id>[0-9]+)/updateTask', views.updateTask, name='newTask'),
    url(r'^(?P<task_id>[0-9]+)/deleteTask', views.deleteTask, name='deleteTask'),
]