from django.contrib import admin
from .models import CrawlingData

class CrawlingDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'update_date']

admin.site.register(CrawlingData, CrawlingDataAdmin)
