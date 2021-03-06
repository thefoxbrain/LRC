from django.conf.urls import patterns
from payment.models import Payment

urlpatterns = patterns('payment.views',
    # ex: /members/
    (r'^$', 'pay_index'),
    # ex: /members/5/
    (r'^(?P<payment_id>\d+)/$', 'pay_detail'),    
    # manage
    (r'^create/(?P<member_id>\d+)/$', 'create_payment'),
    # ex: /payment/manage/1/
    (r'^manage/(?P<payment_id>\d+)/$', 'pay_edit'),
    # ex: /members/5/
    (r'^member/(?P<member_id>\w+)/$', 'pay_member_index'),
    
    (r'^delete/(?P<payment_id>\d+)/?$', 'pay_delete'), 
)