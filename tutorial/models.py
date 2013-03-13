from django.db import models

# tutorial/models.py
class Person(models.Model):
    full_name = models.CharField(max_length=200,  blank=True, verbose_name='full name')
    
    def __unicode__(self):
        return u'%s' % (self.name)
