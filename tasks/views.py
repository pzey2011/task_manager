from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Task, Group

def index(request):
	groups=Group.objects.all()
	return render(request,'tasks/index.html',{ 'groups' :groups })
