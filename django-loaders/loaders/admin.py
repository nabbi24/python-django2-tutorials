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
    list_display = ('form_id', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['form_id']

admin.site.register(CommissionForm, CommissionFormAdmin)

admin.AdminSite.site_header = "Loaders Administration"
