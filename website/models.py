from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blog(models.Model):
	head1=models.CharField(max_length=120,blank=False)
	para1=models.TextField(blank=True)
	para2=models.TextField(blank=True)
	para3=models.TextField(blank=True)
	def __str__(self):
 		return self.head1
