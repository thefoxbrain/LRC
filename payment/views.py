from django.shortcuts import render, get_object_or_404

from members.models import Payment

def pay_index(request):
    latest_payment_list = Payment.objects.all().order_by('-payment_date')[:5]
    context = {'latest_payment_list': latest_payment_list}
    return render(request, 'payment/base_pay_index.html', context)

def pay_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment/base_pay_detail.html', {'payment': payment})
