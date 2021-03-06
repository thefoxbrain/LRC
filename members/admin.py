from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from members.models import Member
from members.models import MembershipType
from payment.models import Payment
from results.models import Event
from results.models import Result
from account.models import LRC

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1
    fields = ('amount','payment_type','payment_date')
    ordering = ['-payment_date']
    
class ResultInline(admin.TabularInline):
    model = Result
    extra = 1
    fields = ('event','boat_class','boat_status','boat_category','crew_members','cox')

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal information', {'fields': [
                                             # 'photo',
                                             'gender',
                                             ('title', 'first_name', 'last_name'),
                                             'date_of_birth',
                                             ('home_phone','mobile_phone'),
                                             'email'                                             
                                             ]}),
        ('Address', {'fields': [
                                             'address_1',
                                             'address_2',
                                             'address_3',
                                             'address_4',
                                             'post_code',
                                             ]}),                 
        ('Emergency Contact Details', {'fields': [
                                            'em_contact_name',
                                            'em_relationship',
                                            'em_contact_no'
                                            ]}),
        ('Class of Membership', {'fields': [
                                            'membership_type',
                                            'payment_method',
                                            ]}),
        ('Previous Rowing experience', {'fields': [
                                            'br_membership_no',
                                            ('rowing_points','sculling_points'),
                                            'capsize_drill',
                                            ]}),
        ('Swimming Ability', {'fields': [
                                            ('swim_50','swim_5_underwater','swim_tread'),
                                            ]}),
        ('Health Questionnaire ', {'fields': [
                                            'health_1_good_health',
                                            'health_1_details',
                                            ]}),
        ('Long-term health conditions ', {'fields': [
                                            ('health_2_diabetes', 'health_2_epilepsy','health_2_asthma'),
                                            ('health_2_dyspraxia','health_2_heart_disease','health_2_other'),
                                            'health_2_details',
                                            ]}),
        ('Other conditions affecting Rowing', {'fields': [
                                            'health_3_other',
                                            'health_3_details',
                                            ]}),
        ('Other health conditions', {'fields': [
                                            'health_4_other',
                                            'health_4_details',
                                            ]}),
        ('Membership confirmation', {'fields': [
                                            'start_date',
                                            'pg_name',
                                            ]}),
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }    
    list_display = ('first_name', 'last_name','start_date','membership_type') 
    list_filter = ['first_name','last_name','membership_type']   
    ordering = ['first_name']
    search_fields = ['first_name','last_name']
    inlines = [PaymentInline] 

admin.site.register(Member, MemberAdmin)

admin.site.register(MembershipType)

class EventAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Event', {'fields': [
                                             # 'photo',
                                             'event_name',
                                             ]}),
        ('Details', {'fields': [
                                             'event_type',
                                             'event_date',
                                             ]}),                 
                     ]
        list_display = ('event_name', 'event_type','event_date')
        list_filter = ['event_name', 'event_type','event_date']
        ordering = ['-event_date']
        inlines = [ResultInline]

admin.site.register(Event,EventAdmin)

class ResultAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Event', {'fields': [
                                             # 'photo',
                                             'event',
                                             ('boat_class','boat_status', 'boat_category'), 
                                             ]}),
        ('Crew', {'fields': [
                                             # 'photo',
                                             'crew_members',
                                             'cox',
                                             ]}),                 
                     ]
        list_display = ('event', 'boat_class','boat_status','boat_category')


admin.site.register(Result,ResultAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount','payment_type','payment_date')
    list_filter = ['member','payment_type','payment_date']
    search_fields = ['member__first_name','member__last_name']
    ordering = ['-payment_date']

admin.site.register(Payment, PaymentAdmin)

class LRCInline(admin.StackedInline):
    model = LRC
    can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (LRCInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)