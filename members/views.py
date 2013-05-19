from django.shortcuts import render, get_object_or_404, redirect,render_to_response,HttpResponse

from members.models import Member,MemberFilter,MemberForm

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

def create_member(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        # pay_mem = Payment.objects.create()
        # return HttpResponseRedirect('payment/member/%i/' % pay_mem.member)
        return redirect('/member/')
    return render(request, 'member/base_member_manage.html', {'form':form})

def member_edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/member/')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = MemberForm(instance=member)
    return render(request, 'member/base_member_manage.html', {'form':form})

def member_export(request):
    from xlwt import Workbook

    wb = Workbook()
    ws = wb.add_sheet('Sheetname')
    ws.write(0, 0, 'first')
    ws.write(0, 1, 'Surname')
    ws.write(1, 0, 'Hans')
    ws.write(1, 1, 'Muster')

    fname = 'testfile.xls'
    response = HttpResponse(mimetype="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % fname

    wb.save(response)

    return response


