from django.conf.urls import patterns, url

from tutorial import views

urlpatterns = patterns('',
    # ex: /members/
    url(r'^$', views.people, name='people'),
)



