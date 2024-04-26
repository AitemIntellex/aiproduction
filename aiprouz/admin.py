from django.contrib import admin
from django.utils import timezone
from .models import DailyReport

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'content')
    fields = ('content',)
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        obj.created_at = timezone.now()  # Устанавливаем текущее время
        super().save_model(request, obj, form, change)
