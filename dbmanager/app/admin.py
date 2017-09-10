from django.contrib import admin

from .models import *

# Register your models here.
class DomainsAdmin(admin.ModelAdmin):
    list_display = ('accession_number', 'id')
admin.site.register(Domains,DomainsAdmin)
class SequencesAdmin(admin.ModelAdmin):
    list_display = ('accession_number', 'id')
admin.site.register(Sequences,SequencesAdmin)