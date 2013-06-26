from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,get_object_or_404,redirect

from results.models import Result,ResultFilter,ResultForm,Event,EventFilter,EventForm

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
    return render(request,'results/base_event_index.html', {'event_list': f})

@permission_required('results.add_result')
def create_result(request,event_id):
    if event_id == '0':
        data = {}
    else:
        event = Event.objects.get(id=event_id)
        data = {'event': event.id}
    form = ResultForm(request.POST or None,initial=data)
    if form.is_valid():
        form.save()
        # pay_mem = Payment.objects.create()
        # return HttpResponseRedirect('payment/member/%i/' % pay_mem.member)
        return redirect('/results/')
    return render(request, 'results/base_result_manage.html', {'form':form})

@permission_required('results.change_result')
def result_edit(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('/results/')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = ResultForm(instance=result)
    return render(request, 'results/base_result_manage.html', {'form':form})

@permission_required('results.add_event')
def create_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        # pay_mem = Payment.objects.create()
        # return HttpResponseRedirect('payment/member/%i/' % pay_mem.member)
        return redirect('/results/event/')
    return render(request, 'results/base_event_manage.html', {'form':form})

@permission_required('results.change_event')
def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/results/event/')
        else:
            print form.errors
    else:
        # create unbound form to display in template
        form = EventForm(instance=event)
    return render(request, 'results/base_event_manage.html', {'form':form})


def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('/results/event/')

def result_delete(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    result.delete()
    return redirect('/results/')