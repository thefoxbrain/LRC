from django.db import models

from django.contrib.auth.models import User

class LRC(models.Model):
    user = models.OneToOneField(User)
    committee_role = models.CharField(max_length=100)
    
    class Meta:
        permissions = (
            ("edit_lrc", "Can make changes to LRC"),
        )