from django.conf.urls import patterns

urlpatterns = patterns('members.views',
    # ex: /members/
    (r'^$', 'member_index'),
    # ex: /members/5/
    (r'^(?P<member_id>\d+)/$', 'member_detail'),    
        
    (r'^membership/(?P<membership_id>\w+)/$', 'member_membership_index'),
)