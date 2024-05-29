#blog/signals.py
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from .models import Post, ActionHistory  , ActivityHistory




@receiver(post_save, sender=Post)
def create_add_or_update_action(sender, instance, created, **kwargs):
    if created:
        action = 'add'
    else:
        action = 'update'
    ActionHistory.objects.create(
        action=action,
        post=instance,
        post_title=instance.title,
        post_description=instance.description,
        post_price=instance.price,
        post_quantity=instance.quantity,
        post_category=instance.category,
        post_trademark=instance.trademark,
        post_image=instance.image,
        # timestamp=timezone.now(),  # Lưu thời gian hành động
    )
@receiver(post_delete, sender=Post)
def create_delete_action(sender, instance, **kwargs):
    ActionHistory.objects.create(
        action='delete',
        post=instance,
        post_title=instance.title,
        post_description=instance.description,
        post_price=instance.price,
        post_quantity=instance.quantity,
        post_category=instance.category,
        post_trademark=instance.trademark,
        post_image=instance.image,
        # timestamp=timezone.now(),  # Lưu thời gian hành động
    )




@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def update_activity_history(sender, instance, **kwargs):
    ActivityHistory.update_quantity_totals()

