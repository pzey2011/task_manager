from django.db import models

class Group(models.Model):
	title = models.CharField(max_length=200)
	def __str__ (self):
		return self.title

class Task(models.Model):
	STATUS = (
		('done', 'done'),
        ('pending', 'pending'),
	)
	title = models.CharField(max_length=200)
	status = models.CharField(max_length=1, choices=STATUS, default='pending')
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	creation_date = models.DateTimeField('date created', auto_now_add=True)
	def __str__ (self):
		return self.title


