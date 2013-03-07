from datetime import date
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
    
class Member(models.Model):
    # Personal Information
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    post_code = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=20,  blank=True)
    mobile_phone = models.CharField(max_length=20,  blank=True)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    
    # Emergency Contact Details
    em_contact_name = models.CharField(max_length=200,  blank=True)
    em_relationship = models.CharField(max_length=200,  blank=True)
    em_contact_no = models.CharField(max_length=200,  blank=True)
    
    # Membership Type
    membership_type = models.ForeignKey(MembershipType)
    
    # Previous Rowing Experience
    br_membership_no = models.CharField(max_length=200,  blank=True)
    rowing_points = models.CharField(max_length=200,  blank=True)
    sculling_points = models.CharField(max_length=200,  blank=True)
    YESNO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    capsize_drill = models.CharField(max_length=1, choices=YESNO_CHOICES)
    
    # Swimming Ability 
    swim_50  = models.CharField(max_length=1, choices=YESNO_CHOICES)
    swim_5_underwater = models.CharField(max_length=1, choices=YESNO_CHOICES)
    swim_tread = models.CharField(max_length=1, choices=YESNO_CHOICES)
    
    # Start Date   
    start_date = models.DateField(("Start Date"), default=date.today)
    
    # Parent \ Guardian
    pg_start_date = models.DateField(("Start Date"), default=date.today,  blank=True)
    pg_name  = models.CharField(max_length=200,  blank=True)
    
    # Health Questionnaire
    health_1_good_health = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_1_details = models.TextField(blank=True)
    
    health_2_diabetes = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_epilepsy = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_asthma = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_dyspraxia = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_heart_disease = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_other = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_2_details  = models.TextField(blank=True)
    
    health_3_other = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_3_details  = models.TextField(blank=True)
    
    health_4_other = models.CharField(max_length=1, choices=YESNO_CHOICES)
    health_4_details  = models.TextField(blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

