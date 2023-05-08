from django.db import models


class Todo(models.Model):

	title = models.CharField(max_length=100)
	details = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50, default='Pending')

	def __str__(self):
		return self.title
