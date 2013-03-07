from django.contrib import admin
from members.models import Member
from members.models import MembershipType 


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','start_date') 
    list_filter = ['first_name','last_name','membership_type']   
    date_hierarchy = 'start_date'
    search_fields = ['first_name','last_name']

admin.site.register(Member, MemberAdmin)

admin.site.register(MembershipType)