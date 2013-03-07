from django.contrib import admin
from members.models import Members
from members.models import MembershipType 

class MembersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information' , {'fields': ['title', 'first_name', 'last_name', 'gender','date_of_birth', 'start_date','email']}),
        ('Membership', {'fields': ['membership_type']}),
    ]
    list_display = ('first_name', 'last_name','started_recently') 
    list_filter = ['first_name','last_name','membership_type']   
    date_hierarchy = 'start_date'
    search_fields = ['first_name','last_name']

admin.site.register(Members, MembersAdmin)

admin.site.register(MembershipType)