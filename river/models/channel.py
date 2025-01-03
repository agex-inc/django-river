from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=500, blank=False)

    class Meta:
        app_label = 'river'
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name.capitalize()
