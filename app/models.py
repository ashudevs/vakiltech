from django.db import models

class ScrapedData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    table_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title


