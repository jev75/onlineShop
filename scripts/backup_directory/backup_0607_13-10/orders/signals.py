from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Order

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'Naujas užsakymas Nr. {instance.id}'
        html_message = render_to_string('orders/order_notification_email.html', {'order': instance})
        plain_message = strip_tags(html_message)
        from_email = 'your_email@example.com'
        to = 'jevgen.vasiljevas@gmail.com'  # Change to your email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
