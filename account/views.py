from django.shortcuts import redirect,render


"""
def member_index(request):
    member_index = Member.objects.all().order_by('-start_date')[:5]
    context = {'member_index': member_index}
    return render(request, 'member/base_index.html', context)
"""    

def account_index(request):
    # return render_to_response('member/base_index.html', {'member_index': f})
    return render(request,'account/account.html')
