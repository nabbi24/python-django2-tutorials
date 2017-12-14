from django.contrib import admin

# Register your models here.
from .models import CommissionForm, Agency

class AgencyInline(admin.TabularInline):
    model = Agency
    extra = 3

class CommissionFormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['form_id']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [AgencyInline]

admin.site.register(CommissionForm, CommissionFormAdmin)
