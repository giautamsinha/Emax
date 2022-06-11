from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import get_connection , EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_token(email, token ,name):
    try:  
        connection = get_connection()
        connection.open() 
        html_content=render_to_string("accounts/email.html",{'name': name , 'email':email , 'token':token})
        text_content=strip_tags(html_content)
        emailSend=EmailMultiAlternatives(
            f'Hello {name} your account need to verified',
            text_content,
            settings.EMAIL_HOST_USER,
            [email, ],
        )
        emailSend.attach_alternative(html_content,"text/html")
        emailSend.send()
        # subject = 'Hello {name} your account need to verified'
        # message = f'Clixck on the link to verify the http://127.0.0.1:8000/account/verify/{token}/'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email, ]
        # send_mail( subject,  email_from, recipient_list )
    except Exception as e:
        return False

    return True
  
def send_password_token(email, token ,name):
    try:  
        connection = get_connection()
        connection.open() 
        html_content=render_to_string("accounts/password_email.html",{'name': name , 'email':email , 'token':token})
        text_content=strip_tags(html_content)
        emailSend=EmailMultiAlternatives(
            f'Hello {name} your reset password OTP',
            text_content,
            settings.EMAIL_HOST_USER,
            [email, ],
        )
        emailSend.attach_alternative(html_content,"text/html")
        emailSend.send()
    except Exception as e:
        return False

    return True