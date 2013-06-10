from django.conf.urls import patterns

urlpatterns = patterns('results.views',
    # ex: /results/
    (r'^$', 'results_index'),
    # ex: /results/5/
    (r'^(?P<result_id>\d+)/$', 'result_detail'),        
    # Events    
    (r'^event/$', 'event_index'),    
    
)