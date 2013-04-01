import django_tables2 as tables
from django_tables2.utils import A

from membership.models import MembershipType

class MembershipTable(tables.Table):
    name = tables.LinkColumn('members.views.member_membership_index', args=[A('id')],orderable=False)
    cost = tables.Column(order_by=("-cost"))
    description = tables.Column(orderable=False)

    
    class Meta:
        model = MembershipType
        fields = ("name", "cost", "description")
        sequence = ("name", "cost", "description")
        order_by=("cost")
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        
    