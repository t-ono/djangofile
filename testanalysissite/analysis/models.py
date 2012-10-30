from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class Subject(models.Model):
	name = models.CharField(max_length=200)
	age  = models.IntegerField()
	#...
	def __unicode__(self):
		return self.name


class Experiment(models.Model):
	subject      = models.ForeignKey(Subject)
	exp_date     = models.DateTimeField('date published')
	exp_datapath = models.CharField(max_length=200)
	# ...
	def __unicode__(self):
		return self.exp_date.strftime('%Y/%m/%d')
	
	#...
	def was_published_today(self):
		return self.exp_date() == datetime.date.today()

class ExperimentInline(admin.StackedInline):
	model = Experiment
	
class SubjectAdmin(admin.ModelAdmin):
	fields = ['name', 'age']
	inlines = [ExperimentInline]
	
class ExperimentAdmin(admin.ModelAdmin):
	fields = ['subject', 'exp_date', 'exp_datapath'];

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Subject, SubjectAdmin)
