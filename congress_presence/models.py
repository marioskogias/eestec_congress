from django.db import models

# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    lc =  models.CharField(max_length=30)
    here = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s from LC %s" % (self.first_name, self.last_name, self.lc)
