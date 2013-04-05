from django.shortcuts import render, get_object_or_404,render_to_response

from members.models import Member,MemberFilter

"""
def member_index(request):
    member_index = Member.objects.all().order_by('-start_date')[:5]
    context = {'member_index': member_index}
    return render(request, 'member/base_index.html', context)
"""    

def member_index(request):
    f = MemberFilter(request.GET, queryset=Member.objects.all().order_by('first_name'))
    return render_to_response('member/base_index.html', {'member_index': f})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/base_detail.html', {'member': member})

def member_membership_index(request, membership_id):
    membership_list = Member.objects.filter(membership_type__id__exact = membership_id).order_by('id')
    return render(request,'member/base_membership_member.html', {'membership_list': membership_list })

"""
def member_membership_index(request, membership_id):
    membership_list = Member.objects.filter(membership_type__id__exact = membership_id).order_by('id')
    return render(request,'member/base_membership_member.html', {'membership_list': membership_list })
"""