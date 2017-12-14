import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class CommissionForm(models.Model):
    form_id = models.CharField(max_length=8, default='')
    pub_date = models.DateTimeField('date published', default=None)
    
    def __str__(self):
        return self.form_id

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Agency(models.Model):
    commission_form = models.ForeignKey(
        CommissionForm,
        on_delete=models.CASCADE
    )
    agency_id = models.CharField(max_length=12, default='')
    area = models.IntegerField(default=0)

    def __str__(self):
        return self.agency_id

