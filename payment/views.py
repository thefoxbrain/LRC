from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect

from members.models import Payment,PaymentForm

def pay_index(request):
    latest_payment_list = Payment.objects.all().order_by('-id')
    context = {'latest_payment_list': latest_payment_list}
    return render(request, 'payment/base_pay_index.html', context)

def pay_member_index(request, member_id):
    member_payment_list = Payment.objects.filter(member__id__exact = member_id).order_by('id')
    return render(request,'payment/base_pay_member_index.html', {'member_payment_list': member_payment_list })

def pay_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment/base_pay_detail.html', {'payment': payment})


def create_payment(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        # pay_mem = Payment.objects.create()
        # return HttpResponseRedirect('payment/member/%i/' % pay_mem.member)
        return redirect('/payment/')
    return render(request, 'payment/base_pay_manage.html', {'form':form})

def pay_edit(request, payment_id):
    pay = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=pay)
        if form.is_valid():
            return redirect('/payment/')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = PaymentForm(instance=pay)
    return render(request, 'payment/base_pay_manage.html', {'form':form})


"""
def update_notification_preference(request, object_id):
    np = get_object_or_404(NotificationPreference, pk=object_id)
    if request.method == 'POST':
        form = NotificationPreferenceForm(request.POST, instance=np)
        if form.is_valid():
            obj = form.save(commit=False)
            # Add the owner of the record for access control
            obj.owner = request.user.email
            form.save()
            return redirect('/notification_preference/list')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = NotificationPreferenceForm(instance=np)
    return render(request, 'notification_preference/save.html', {'np': np, 'form':form,'notification_preference':NotificationPreference})
"""