from django.conf.urls import patterns

urlpatterns = patterns('account.views',
    # ex: /members/
    (r'^$', 'account_index'),
)