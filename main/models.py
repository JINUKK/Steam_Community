from django.db import models

# Create your models here.

class CrawlingData(models.Model):
    title = models.CharField(max_length=50, blank=True)
    html_data = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title + self.update_date.strftime('%Y.%m.%d %H:%M')