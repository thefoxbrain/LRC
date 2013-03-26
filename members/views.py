from django.shortcuts import render, get_object_or_404

from members.models import Member

def index(request):
    latest_member_list = Member.objects.all().order_by('-start_date')[:5]
    context = {'latest_member_list': latest_member_list}
    return render(request, 'member/base_index.html', context)

def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/base_detail.html', {'member': member})

def membership_index(request, membership_id):
    membership_list = Member.objects.filter(membership_type__id__exact = membership_id).order_by('id')
    return render(request,'member/base_membership_member.html', {'membership_list': membership_list })
