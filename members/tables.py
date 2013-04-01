import django_tables2 as tables
from django_tables2.utils import A

from members.models import Member

class MemberTable(tables.Table):
    first_name = tables.LinkColumn('members.views.member_detail', args=[A('id')])
    last_name = tables.LinkColumn('members.views.member_detail', args=[A('id')])
    membership_type = tables.LinkColumn('members.views.member_membership_index', args=[A('membership_type.id')])
    payments = tables.TemplateColumn('<a href="/payment/member/{{ record.id }}"><img src="{{ STATIC_URL }}history.png" alt="Payment History" width=24 length=24></a>',orderable=False)
    email = tables.Column(orderable=False)  
    
    class Meta:
        model = Member
        fields = (
                  "first_name", 
                  "last_name",
                  "membership_type",
                  "email"
                  )
        order_by = ("last_name")
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}