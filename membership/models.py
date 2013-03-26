from django.db import models

class MembershipType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,  blank=True)
    cost = models.IntegerField(default=0)
    list_display = ('name', 'description')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']