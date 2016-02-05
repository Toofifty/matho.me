from django.contrib import admin

from .models import UrlRecord

class UrlRecordAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'redirect_to', 'redirects')
    search_fields = ['short_url', 'long_url', 'user']
    
admin.site.register(UrlRecord, UrlRecordAdmin)