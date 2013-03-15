from django.shortcuts import render, get_object_or_404

from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from members.models import Member


urlpatterns = patterns('',
    (r'^member/$', ListView.as_view(
        model=Member,
    )),
)




def index(request):
    latest_member_list = Member.objects.all().order_by('-start_date')[:5]
    context = {'latest_member_list': latest_member_list}
    return render(request, 'member/index.html', context)

def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/detail.html', {'member': member})
