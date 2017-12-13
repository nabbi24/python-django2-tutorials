from django.db import models

# Create your models here.
class CommissionForm(models.Model):
    form_id = models.CharField(max_length=8, default='')
    pub_date = models.DateTimeField('date published', default=None)
    
    def __str__(self):
        return self.form_id

class Agency(models.Model):
    commission_form = models.ForeignKey(
        CommissionForm,
        on_delete=models.CASCADE
    )
    agency_id = models.CharField(max_length=12, default='')
    area = models.IntegerField(default=0)

    def __str__(self):
        return self.agency_id

