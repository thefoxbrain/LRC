from django.shortcuts import render, get_object_or_404,render_to_response

from membership.models import MembershipType
from members.models import Member

def membership_index(request):
    # membership_list = MembershipType.objects.all().order_by('-cost')
    membership_list = MembershipType.objects.all()
    context = {'membership_list': membership_list}
    return render(request, 'membership/base_membership_index.html', context)

def membership_detail(request, membership_id):
    membership = get_object_or_404(MembershipType, pk=membership_id)
    return render(request, 'membership/base_membership_detail.html', {'membership': membership})

def membership_chart(request):
    model = MembershipType.objects.all()
    xdata = []
    ydata = []
    for i in model:
        xname = i.name
        ycount = Member.objects.filter(membership_type=i).count()
        # xname = u'%s %s' % (xname, ycount)
        
        xdata.append(xname)
        ydata.append(ycount)
        
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('membership/base_membership_chart.html', data)

"""
def membership_index(request):
    membership_list = MembershipTable(MembershipType.objects.all())
    # RequestConfig(request, paginate={"per_page": 5}).configure(membership_list)
    RequestConfig(request).configure(membership_list)
    return render(request, 'membership/base_membership_index.html', {'membership_list': membership_list})
"""