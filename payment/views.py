from django.shortcuts import render, get_object_or_404,render_to_response

from members.models import Payment

def pay_index(request):
    latest_payment_list = Payment.objects.all().order_by('-payment_date')[:5]
    context = {'latest_payment_list': latest_payment_list}
    return render(request, 'payment/base_pay_index.html', context)
"""
def pay_member_index(request):
    member_payment_list = Payment.objects.filter(member__id = 1)
    context = {'member_payment_list': member_payment_list}
    return render(request, 'payment/base_pay_member_index.html', context)
"""    

def pay_member_index(request, last_name):
    member_payment_list = Payment.objects.filter(member__last_name__exact = last_name)
    return render_to_response('payment/base_pay_member_index.html', {'member_payment_list': member_payment_list })

def pay_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment/base_pay_detail.html', {'payment': payment})
