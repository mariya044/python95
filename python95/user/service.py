from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "Thanks for registrations",
        "nice to meet you",
        'EMAIL_HOST_USER',
        [user_email],
        fail_silently=False,
    )