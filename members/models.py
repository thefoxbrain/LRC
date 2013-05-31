from datetime import date
# from PIL import Image
from django.db import models
from django.forms import ModelForm
import django_filters

from membership.models import MembershipType

FILTER_PAYMENTMETHOD_CHOICES = (
    ('', 'All'),
    ('S', 'Standing Order'),
    ('Q', 'Cheque'),
    ('C', 'Cash'),
    ('B', 'Bank Transfer'),
    )
    
class Member(models.Model):
    # Personal Information
    # photo = models.ImageField(upload_to='members_photos')
    TITLE_CHOICES = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MISS', 'Miss'),
        ('MS', 'Ms'),
        ('DR', 'Dr'),
    )
    title = models.CharField(max_length=4, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address_1 = models.CharField(max_length=200,  blank=True, verbose_name='Address Line 1')
    address_2 = models.CharField(max_length=200,  blank=True, verbose_name='Address Line 2')
    address_3 = models.CharField(max_length=200,  blank=True, verbose_name='Town/City')
    address_4 = models.CharField(max_length=200,  blank=True, verbose_name='County')
    post_code = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=20,  blank=True)
    mobile_phone = models.CharField(max_length=20,  blank=True)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    
    # Emergency Contact Details
    em_contact_name = models.CharField(max_length=200,  blank=True, verbose_name='Emergency Contact Name')
    em_relationship = models.CharField(max_length=200,  blank=True, verbose_name='Relationship to Participant')
    em_contact_no = models.CharField(max_length=200,  blank=True, verbose_name='Emergency Contact Number')
    
    # Membership Type
    membership_type = models.ForeignKey(MembershipType, related_name="types")
    
    # Previous Rowing Experience
    br_membership_no = models.CharField(max_length=200,  blank=True, verbose_name='BR Membership number')
    rowing_points = models.IntegerField(default=0, blank=True)
    sculling_points = models.IntegerField(default=0, blank=True)
    YESNO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    capsize_drill = models.CharField(max_length=1, choices=YESNO_CHOICES,default='N',blank=True)
    
    # Swimming Ability 
    swim_50  = models.CharField(max_length=1, choices=YESNO_CHOICES, default='Y', blank=True,verbose_name='50 metres')
    swim_5_underwater = models.CharField(max_length=1, choices=YESNO_CHOICES,default='Y', blank=True,verbose_name='5 metres underwater')
    swim_tread = models.CharField(max_length=1, choices=YESNO_CHOICES, default='Y', blank=True,verbose_name='Tread water for 2 minutes')
    
    # Start Date   
    start_date = models.DateField(("Start Date"), default=date.today)
    
    # Parent \ Guardian
    pg_name  = models.CharField(max_length=200,  blank=True, verbose_name='Parent \ Guardian')
    
    # Health Questionnaire
    health_1_good_health = models.CharField(max_length=1, choices=YESNO_CHOICES, default='Y', verbose_name='Good general health?')
    health_1_details = models.TextField(blank=True, verbose_name='if No - details')
    
    health_2_diabetes = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Diabetes')
    health_2_epilepsy = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Epilepsy')
    health_2_asthma = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Asthma')
    health_2_dyspraxia = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Dyspraxia')
    health_2_heart_disease = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Heart Disease')
    health_2_other = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Other')
    health_2_details  = models.TextField(blank=True, verbose_name='if Yes - details')
    
    health_3_other = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N', verbose_name='Other conditions affecting Rowing?')
    health_3_details  = models.TextField(blank=True, verbose_name='if Yes - details')
    
    health_4_other = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N',verbose_name='Other health conditions?')
    health_4_details  = models.TextField(blank=True, verbose_name='if Yes - details')
    PAYMENTMETHOD_CHOICES = (
        ('S', 'Standing Order'),
        ('Q', 'Cheque'),
        ('C', 'Cash'),
        ('B', 'Bank Transfer'),
    )
    
    payment_method = models.CharField(max_length=1, choices=PAYMENTMETHOD_CHOICES,blank=True)
    full_name = models.CharField(max_length=200,  blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def save(self, *args, **kwargs):
        self.full_name = '%s %s' % (self.first_name, self.last_name)
        super(Member, self).save(*args, **kwargs)    
    
class MemberFilter(django_filters.FilterSet):
    full_name = django_filters.AllValuesFilter()
    payment_method = django_filters.ChoiceFilter(choices=FILTER_PAYMENTMETHOD_CHOICES, label='Payment Method')
        
    class Meta:
        model = Member
        fields = ['full_name', 'payment_method', 'membership_type']
        
    def __init__(self, *args, **kwargs):
                super(MemberFilter, self).__init__(*args, **kwargs)
                self.filters['membership_type'].extra.update(
                    {'empty_label': 'All'})         
        
class MemberForm(ModelForm):

    class Meta:
        model = Member
        # fields = ['first_name', 'last_name','date_of_birth']     
        

