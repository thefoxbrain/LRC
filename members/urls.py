from django.conf.urls import patterns

urlpatterns = patterns('members.views',
    # ex: /members/
    (r'^$', 'member_index'),
    # ex: /members/5/
    (r'^(?P<member_id>\d+)/$', 'member_detail'),
    # create new member    
    (r'^manage/$', 'create_member'),
    # edit member
    (r'^manage/(?P<member_id>\d+)/$', 'member_edit'),
    # list of members of a certain type
    (r'^membership/(?P<membership_id>\w+)/$', 'member_membership_index'),
    # list of members of a certain type
    (r'^export/$', 'member_export'),    
)