import django_tables2 as tables
from django_tables2.utils import A

from payment.models import Payment

class PaymentTable(tables.Table):
    member = tables.LinkColumn('members.views.member_detail', args=[A('member.id')],orderable=False)
    history = tables.TemplateColumn('<a href="/payment/member/{{ record.member.id }}"><img src="{{ STATIC_URL }}history.png" alt="Payment History" width=24 length=24></a>',orderable=False)
    edit = tables.TemplateColumn('<a href="/payment/manage/{{ record.id }}"><img src="{{ STATIC_URL }}edit.png" alt="Payment History" width=24 length=24></a>',orderable=False)
    delete = tables.TemplateColumn('<a href="/payment/delete/{{ record.id }}"><img src="{{ STATIC_URL }}delete.png" alt="Payment History" width=24 length=24></a>',orderable=False)
    payment_type = tables.Column(orderable=False)  
    amount = tables.Column(orderable=False)
    payment_date = tables.DateColumn('d/m/Y')  
  
    class Meta:
        model = Payment
        fields = (
                  "payment_date", 
                  "member",
                  "payment_type",
                  "amount",
                  "history",
                  "edit",
                  "delete"                
                  )
        order_by = ("-payment_date")
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}