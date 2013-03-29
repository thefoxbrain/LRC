from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig

from membership.models import MembershipType
from membership.tables import MembershipTable

def membership_index(request):
    membership_list = MembershipTable(MembershipType.objects.all())
    # RequestConfig(request, paginate={"per_page": 5}).configure(membership_list)
    RequestConfig(request).configure(membership_list)
    return render(request, 'membership/base_membership_index.html', {'membership_list': membership_list})

"""
def people(request):
    return render(request, "people.html", {"people": Person.objects.all()})
"""

def membership_detail(request, membership_id):
    membership = get_object_or_404(MembershipType, pk=membership_id)
    return render(request, 'membership/base_membership_detail.html', {'membership': membership})