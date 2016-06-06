from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Professor(models.Model):
	name = models.CharField(max_length=200)

class ProfessorUnavailability(models.Model):
	day = models.CharField(max_length=1)
	start_time = models.CharField(max_length=5)
	end_time = models.CharField(max_length=5)
	preference_level = models.IntegerField(default=0)
	professor = models.ForeignKey(Professor)

class Room(models.Model):
	building = models.CharField(max_length=100)
	number = models.CharField(max_length=10)
	capacity = models.IntegerField()

class Course(models.Model):
	number = models.CharField(max_length=10)

class Section(models.Model):
	capacity = models.IntegerField()
	professor = models.ForeignKey(Professor)
	course = models.ForeignKey(Course)

class Offering(models.Model):
	duration = models.IntegerField()
	section = models.ForeignKey(Section)
