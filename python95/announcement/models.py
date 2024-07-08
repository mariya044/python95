from django.db import models

from user.models import NewUser


class Announcement(models.Model):
    CHOICES = (
        ('+', "+"),
        ("-", "-")
    )
    LEVELS=(
    ('Начальный',"Начальный'"),
    ("Средний","Средний"),
    ("Продвинутый","Продвинутый"),
    )
    CURRENCY = (
        ("USD", "USD"),
        ("BYN", "BYN"),
        ("RUB", "RUB"),
    )
    SUBJECTS=(
        ('English',"English"),
        ("Russian","Russian"),
        ("Math","Math"),
        ("History","History"),
        ('Belarusian',"Belarusian"),
        ('Chemistry',"Chemistry"),
        ('Physics',"Physics")
    )
    first_name=models.CharField(max_length=50,null=False, blank=False)
    form=models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=100, choices=SUBJECTS, default="English", null=False, blank=False)
    age=models.IntegerField(null=False, blank=False)
    city=models.CharField(max_length=50,null=False, blank=False)
    address=models.CharField(max_length=150,null=False, blank=False)
    price_limit_from=models.IntegerField(null=False, blank=False)
    price_limit_to=models.IntegerField(null=False, blank=False)
    online_lessons = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    offline_lessons = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    lessons_at_home = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    level_of_knowledge=models.CharField(max_length=100, choices=LEVELS, default="+", null=False, blank=False)
    phone_number=models.CharField(null=True, blank=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, choices=CURRENCY, default="BYN", null=False, blank=False)
