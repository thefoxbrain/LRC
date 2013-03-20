from django.conf.urls import patterns

urlpatterns = patterns('members.views',
    # ex: /members/
    (r'^$', 'index'),
    # ex: /members/5/
    (r'^(?P<member_id>\d+)/$', 'detail'),    
)