from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect

from membership.models import MembershipType

def membership_index(request):
    membership_list = MembershipType.objects.all()
    context = {'membership_list': membership_list}
    return render(request, 'membership/base_membership_index.html', context)

def membership_detail(request, membership_id):
    membership = get_object_or_404(MembershipType, pk=membership_id)
    return render(request, 'membership/base_membership_detail.html', {'membership': membership})