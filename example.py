from django.conf import settings
from django.core.mail import send_mail


send_mail('subject', 'code', from_email=settings.EMAIL_HOST_USER, recipient_list=['mr2006dev@gmail.com'])