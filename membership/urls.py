from django.conf.urls import patterns

urlpatterns = patterns('',
    # ex: /members/
    (r'^$', 'membership.views.membership_index'),
    # ex: /members/5/
    (r'^(?P<membership_id>\d+)/$', 'membership.views.membership_detail'),    
)