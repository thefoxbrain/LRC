from django.shortcuts import render, get_object_or_404, redirect,render_to_response

from payment.models import Payment,PaymentForm,PaymentFilter

def pay_index(request):
    f = PaymentFilter(request.GET, queryset=Payment.objects.all().order_by('-payment_date'))
    # return render_to_response('payment/base_pay_index.html', {'payment_list': f})
    return render(request,'payment/base_pay_index.html', {'payment_list': f})


def pay_member_index(request, member_id):
    member_payment_list = Payment.objects.filter(member__id__exact = member_id).order_by('-payment_date')
    return render(request,'payment/base_pay_member_index.html', {'member_payment_list': member_payment_list })

def pay_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment/base_pay_detail.html', {'payment': payment})

def pay_delete(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    payment.delete()
    return redirect('/payment/')


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
            form.save()
            return redirect('/payment/')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = PaymentForm(instance=pay)
    return render(request, 'payment/base_pay_manage.html', {'form':form})