from django.shortcuts import render,get_object_or_404

from results.models import Result,ResultFilter,Event,EventFilter

def results_index(request):
    f = ResultFilter(request.GET, queryset=Result.objects.all())
    # return render_to_response('payment/base_pay_index.html', {'payment_list': f})
    return render(request,'results/base_result_index.html', {'result_list': f})# Create your views here.

def result_detail(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    return render(request, 'results/base_result_detail.html', {'result': result})

def event_index(request):
    f = EventFilter(request.GET, queryset=Event.objects.all())
    # return render_to_response('payment/base_pay_index.html', {'payment_list': f})
    return render(request,'results/base_event_index.html', {'event_list': f})# Create your views here.