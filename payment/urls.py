from django.conf.urls import patterns

urlpatterns = patterns('payment.views',
    # ex: /members/
    (r'^$', 'pay_index'),
    # ex: /members/5/
    (r'^(?P<payment_id>\d+)/$', 'pay_detail'),    
)