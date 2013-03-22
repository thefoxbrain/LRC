from django.shortcuts import render, get_object_or_404,render_to_response
from django.forms.models import modelformset_factory

from members.models import Payment

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

def pay_manage(request):
    PaymentFormSet = modelformset_factory(Payment)
    if request.method == 'POST':
        formset = PaymentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = PaymentFormSet()
    return render_to_response("payment/base_pay_manage.html", {
        "formset": formset,
    })