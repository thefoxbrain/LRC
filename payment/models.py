from django.db import models
from django.forms import ModelForm
from django import forms
import django_filters
import datetime

from members.models import Member

FILTER_PAYMENTTYPE_CHOICES = (
    ('', 'All'),
    ('S', 'Standing Order'),
    ('Q', 'Cheque'),
    ('C', 'Cash'),
    ('B', 'Bank Transfer'),
    )


class Payment(models.Model):
    member = models.ForeignKey(Member, related_name="payments",blank=False)
    payment_note = models.CharField(max_length=200,blank=True)
    amount = models.CharField(max_length=200, verbose_name='Amount',blank=False)
    payment_date = models.DateField()
    PAYMENTTYPE_CHOICES = (
        ('S', 'Standing Order'),
        ('Q', 'Cheque'),
        ('C', 'Cash'),
        ('B', 'Bank Transfer'),
    )
    payment_type = models.CharField(max_length=1, choices=PAYMENTTYPE_CHOICES,blank=False)
    
    def __unicode__(self):
        return u'%s' % (self.member)
    
  
class PaymentForm(ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.order_by('full_name'))
    payment_note = forms.CharField(widget=forms.Textarea,required=False)
    payment_date = forms.DateField(initial=datetime.date.today)
    amount = forms.CharField()
        
    class Meta:
        model = Payment
        fields = ['member', 'payment_date','amount','payment_type','payment_note']
        
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['payment_note'].widget.attrs['rows'] = 5
        self.fields['payment_note']        
        
class PaymentFilter(django_filters.FilterSet):
    # member = forms.ModelChoiceField(queryset=Member.objects.order_by('full_name'))
    # member = django_filters.ModelChoiceFilter(queryset=Payment.objects.order_by('-member'))
    member = django_filters.ModelChoiceFilter(queryset=Member.objects.order_by('full_name'))
    payment_type = django_filters.ChoiceFilter(choices=FILTER_PAYMENTTYPE_CHOICES, label='Payment Type')
        
    class Meta:
        model = Payment
        fields = ['member','payment_type']
        order_by = ('member')
        
