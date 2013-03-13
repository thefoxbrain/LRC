from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin

from members.models import Member
from members.models import MembershipType
from tutorial.models import Person 


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal information', {'fields': [
                                             # 'photo',
                                             'gender',
                                             ('title', 'first_name', 'last_name'),
                                             'date_of_birth',
                                             'address',
                                             'post_code',
                                             ('home_phone','mobile_phone'),
                                             'email'                                             
                                             ]}),
        ('Emergency Contact Details', {'fields': [
                                            'em_contact_name',
                                            'em_relationship',
                                            'em_contact_no'
                                            ]}),
        ('Class of Membership', {'fields': [
                                            'membership_type',
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
    date_hierarchy = 'start_date'
    search_fields = ['first_name','last_name']

admin.site.register(Member, MemberAdmin)

admin.site.register(MembershipType)

admin.site.register(Person)