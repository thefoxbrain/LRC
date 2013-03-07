from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',
    # ex: /members/
    url(r'^$', views.index, name='index'),
    # ex: /members/5/
    url(r'^(?P<member_id>\d+)/$', views.detail, name='detail'),    

)