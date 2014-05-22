from django.db import models

# Create your models here.
class Question(models.Model):
    text= models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField()
    def __unicode__(self):
        return self.choice_text
