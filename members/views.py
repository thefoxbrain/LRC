from django.shortcuts import render, get_object_or_404

from django_tables2 import RequestConfig

from members.models import Member
from members.tables import MemberTable

def member_index(request):
    member_list = MemberTable(Member.objects.all())
    RequestConfig(request, paginate={"per_page": 5}).configure(member_list)
    return render(request, 'member/base_index.html', {'member_list': member_list})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/base_detail.html', {'member': member})

def member_membership_index(request, membership_id):
    membership_list = MemberTable(Member.objects.filter(membership_type__id__exact = membership_id))
    RequestConfig(request, paginate={"per_page": 5}).configure(membership_list)
    return render(request,'member/base_membership_member.html', {'membership_list': membership_list })

"""
def member_membership_index(request, membership_id):
    membership_list = Member.objects.filter(membership_type__id__exact = membership_id).order_by('id')
    return render(request,'member/base_membership_member.html', {'membership_list': membership_list })
"""