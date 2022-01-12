from django.contrib import admin
from .models import RecentActivity

class RecentActivityAdmin(admin.ModelAdmin):
    list_display = ('query', 'device', 'secret_ip', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('query', 'device', 'secret_ip')

admin.site.site_header = "مدیریت اردک اردک برو"
admin.site.site_title = admin.site.site_header
admin.site.index_title = "به پنل مدیریت دیتابیس اردک اردک برو خوش آمدید"
admin.site.register(RecentActivity, RecentActivityAdmin)