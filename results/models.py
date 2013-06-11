from django.db import models
import django_filters

from members.models import Member

FILTER_EVENTTYPE_CHOICES = (
    ('', 'All'),
    ('H', 'Head Race'),
    ('R', 'Regatta'),
    )

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    EVENTTYPE_CHOICES = (
        ('H', 'Head Race'),
        ('R', 'Regatta'),
    )
    event_type = models.CharField(max_length=1, choices=EVENTTYPE_CHOICES)
    event_date = models.DateField()
    
    def __unicode__(self):
        return self.event_name    
    
class EventFilter(django_filters.FilterSet):
    event_name = django_filters.ModelChoiceFilter(queryset=Event.objects.order_by('-event_date'))
    event_type = django_filters.ChoiceFilter(choices=FILTER_EVENTTYPE_CHOICES, label='Event Type')
    event_date = django_filters.DateFilter(lookup_type='gt')
        
    class Meta:
        model = Event
        fields = ['event_name','event_type','event_date']        


class Result(models.Model):
    event = models.ForeignKey(Event, related_name="event")
    BOATCLASS_CHOICES = (
        ('1', 'Open'),
        ('2', 'Women'),
        ('3', 'Junior'),
        ('4', 'Master')
        )    
    boat_class = models.CharField(max_length=1, choices=BOATCLASS_CHOICES)
    
    BOATCAT_CHOICES = (
        ('1', '1x'),
        ('2', '2-'),
        ('3', '2x'),
        ('4', '4+'),
        ('5', '4+'),
        ('6', '4x-'),
        ('7', '4x+'),
        ('8', '8+')
        )
    boat_category = models.CharField(max_length=1, choices=BOATCAT_CHOICES)

    BOATSTATUS_CHOICES = (
        ('1', 'NOV'),
        ('2', 'IM3'),
        ('3', 'IM2'),
        ('4', 'IM1'),
        ('5', 'SEN'),
        ('6', 'ELI'),
        ('7', 'PRI'),
        ('8', 'J12'),
        ('9', 'J13'),
        ('A', 'J14'),
        ('B', 'J15'),
        ('C', 'J16'),
        ('D', 'J17'),
        ('E', 'J18'),
        ('F', 'MasA'),
        ('G', 'MasB'),
        ('H', 'MasC'),
        ('I', 'MasD'),
        ('J', 'MasE'),
        ('K', 'MasF'),
        ('L', 'MasG')
        )
    boat_status = models.CharField(max_length=1, choices=BOATSTATUS_CHOICES)

    crew_1 = models.ForeignKey(Member, related_name="crew_1")
    crew_2 = models.ForeignKey(Member, related_name="crew_2",null=True,  blank=True)
    crew_3 = models.ForeignKey(Member, related_name="crew_3",null=True,  blank=True)
    crew_4 = models.ForeignKey(Member, related_name="crew_4",null=True,  blank=True)
    crew_5 = models.ForeignKey(Member, related_name="crew_5", null=True, blank=True)
    crew_6 = models.ForeignKey(Member, related_name="crew_6",null=True,  blank=True)
    crew_7 = models.ForeignKey(Member, related_name="crew_7", null=True, blank=True)
    crew_8 = models.ForeignKey(Member, related_name="crew_8", null=True, blank=True)
    cox = models.ForeignKey(Member, related_name="cox",null=True,  blank=True)
    crew_members = models.ManyToManyField(Member) 

class ResultFilter(django_filters.FilterSet):
    event = django_filters.ModelChoiceFilter(queryset=Event.objects.order_by('-event_date'))
    crew_members = django_filters.ModelChoiceFilter(queryset=Member.objects.order_by('full_name')) 
        
    class Meta:
        model = Result
        fields = ['event','crew_members']
        
    
