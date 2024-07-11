from django.db import models

from user.models import NewUser


class Subject(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.subject


class Announcement(models.Model):
    CHOICES = (
        ('+', "+"),
        ("-", "-")
    )
    LEVELS=(
    ('Elementary(A1)',"Elementary(A1"),
    ("Pre-Intermediate(A2)","Pre-Intermediate(A2"),
    ("Intermediate(B1)","Intermediate(B1)"),
    ('Upper-Intermediate(B2)','Upper-Intermediate(B2)'),
    ('Advanced(C1,C2)','Advanced(C2)'),
    )
    CURRENCY = (
        ("USD", "USD"),
        ("BYN", "BYN"),
        ("RUB", "RUB"),
    )
    first_name=models.CharField(max_length=50,null=False, blank=False)
    form=models.IntegerField(null=True, blank=True)
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
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name
