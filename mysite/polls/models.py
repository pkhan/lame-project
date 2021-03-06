from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
    """
    The poll question being asked
    """
    #I am a minor change
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def opened_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    #something else
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    #I am a different minor change
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text

    def nsfw(self):
        return self.choice_text.find("butt") > -1 
