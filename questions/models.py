from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
  name = models.CharField(max_length=60)
  creator = models.ForeignKey('auth.User')
  # has_many questions (see below)

  def __unicode__(self):
    return self.name

class Question(models.Model):
  question = models.CharField(max_length=100) # Maybe bigger?
  details = models.TextField(blank=True) # blank=True means not required (allowed to be blank)
  quiz = models.ForeignKey('Quiz')
  # has_many choices (see below)

  # This is the name as it appears in listings
  def __unicode__(self):
    return self.question

class Choice(models.Model):
  code = models.CharField(max_length=3) # Eg. A or 1 or C
  text = models.CharField(max_length=100) # Maybe bigger?
  question = models.ForeignKey('Question', related_name='choices')
  correct = models.BooleanField('Correct?')

  def __unicode__(self):
    return self.code + ": " + self.text #eg. "A: Spain"
