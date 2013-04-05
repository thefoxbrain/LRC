from django.db import models
from django.forms import ModelForm
from django import forms
import django_filters

from members.models import Member


class Payment(models.Model):
    member = models.ForeignKey(Member)
    payment_note = models.CharField(max_length=200,blank=True)
    amount = models.CharField(max_length=200, verbose_name='Amount')
    payment_date = models.DateField()
    PAYMENTTYPE_CHOICES = (
        ('S', 'Standing Order'),
        ('Q', 'Cheque'),
        ('C', 'Cash'),
        ('B', 'Bank Transfer'),
    )
    payment_type = models.CharField(max_length=1, choices=PAYMENTTYPE_CHOICES,blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.member)
    
class PaymentForm(ModelForm):
    payment_note = forms.CharField(widget=forms.Textarea)
    payment_date = forms.DateInput()
    class Meta:
        model = Payment
        fields = ['member', 'payment_date','amount','payment_type','payment_note']
        
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['payment_note'].widget.attrs['rows'] = 5
        self.fields['payment_note']        
        
class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['payment_date', 'member', 'payment_type']        