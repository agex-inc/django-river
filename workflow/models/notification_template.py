from django.db import models
from workflow.models import Function, Template

class NotificationTemplate(models.Model):
    function = models.ForeignKey(Function, related_name='notification_templates', on_delete=models.CASCADE)
    template = models.ForeignKey(Template, related_name='notification_templates', on_delete=models.CASCADE)

    class Meta:
        app_label = 'workflow'
        verbose_name = "Notification Template"
        verbose_name_plural = "Notification Templates"

    def __str__(self):
        return self.function.name + " - " + self.template.name