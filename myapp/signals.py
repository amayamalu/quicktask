
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def log_task_activity(sender, instance, created, **kwargs):
    if created:
        print(f"Task created by {instance.created_by.username}")
    else:
        print(f"Task updated by {instance.updated_by.username}")
