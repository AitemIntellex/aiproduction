from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

class DailyReport(models.Model):
    content = models.CharField(max_length=200, verbose_name="Content")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at")

    def __str__(self):
        return f"Report for {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Daily report"
        verbose_name_plural = "Daily repots"
