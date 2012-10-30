from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #...
    def __unicode__(self):
        return self.question
    #...
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

#class PollAdmin(admin.ModelAdmin):
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
#    ]


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    # ...
    def __unicode__(self):
        return self.choice

class ChoiceInline(admin. TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question']}),
        ('Date information', {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]


#admin.site.register(Choice)
admin.site.register(Poll,PollAdmin)
