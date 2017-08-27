from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Task, Group

def index(request):
	groups=Group.objects.all()
	return render(request,'tasks/index.html',{ 'groups' :groups })

def newGroup(request):
	Group.objects.create(title=request.POST["name"])
	return HttpResponseRedirect('/tasks')

def newTask(request, group_id):
	Task.objects.create(title=request.POST["name"],group=get_object_or_404(Group,pk=group_id))
	return HttpResponseRedirect('/tasks')

def updateTask(request, group_id, task_id):
	group=get_object_or_404(Group,pk=group_id)
	task= get_object_or_404(Task,pk=task_id)
	if request.POST["radio"]=="1" :
		task.status="pending"
	else:
		task.status="done"
	task.save()
	return HttpResponseRedirect('/tasks')

def deleteTask(request, task_id):
	task = get_object_or_404(Task,pk=task_id)
	if task.status == "pending":
		task.delete()
	
	return HttpResponseRedirect('/tasks')

