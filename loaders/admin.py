from django.contrib import admin

# Register your models here.
from .models import CommissionForm

class CommissionFormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['form_id']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]

admin.site.register(CommissionForm, CommissionFormAdmin)
