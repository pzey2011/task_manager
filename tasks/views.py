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

