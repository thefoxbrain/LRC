import datetime
from django.utils import timezone
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
    
class Members(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    email = models.EmailField(blank=True, verbose_name='e-mail')
    membership_type = models.ForeignKey(MembershipType)
    start_date = models.DateTimeField('Start Date')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def started_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)
    started_recently.admin_order_field = 'start_date'
    started_recently.boolean = True
    started_recently.short_description = 'Started recently?'
