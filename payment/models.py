from django.db import models
from django.forms import ModelForm

from members.models import Member


class Payment(models.Model):
    member = models.ForeignKey(Member)
    payment_note = models.CharField(max_length=200)
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
    class Meta:
        model = Payment            