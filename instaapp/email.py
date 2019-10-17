from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the instagram update'
    sender = 'joselynejojo740@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"username": username})
    html_content = render_to_string('email/newsemail.html',{"username": username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()