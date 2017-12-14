from django.contrib import admin

# Register your models here.
from .models import CommissionForm

class CommissionFormAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'form_id']

admin.site.register(CommissionForm, CommissionFormAdmin)
