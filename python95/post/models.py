from django.db import models

from user.models import NewUser



class Post(models.Model):
    REQUIRED_FIELDS = ('user',)
    SUBJECTS=(
        ('English',"English"),
        ("Russian","Russian"),
        ("Math","Math"),
        ("History","History"),
        ('Belarusian',"Belarusian"),
        ('Chemistry',"Chemistry"),
        ('Physics',"Physics")
    )
    CHOICES=(
        ('+',"+"),
        ("-","-")
    )
    TIME=(
        ('30',"30"),
        ("45","45"),
        ("60","60"),
        ("90","90"),
    )
    CURRENCY=(
        ("USD","USD"),
        ("BYN","BYN"),
        ("RUB","RUB"),
    )

    image = models.ImageField(null=False, blank=False, upload_to="images")
    first_name = models.CharField(max_length=100, null=False, blank=False)
    second_name = models.CharField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECTS, default="English", null=False, blank=False)
    about = models.TextField(max_length=500, blank=True, null=True)
    qualification = models.CharField(max_length=200, null=False, blank=False)
    work_experience = models.CharField(max_length=300, null=False, blank=False, )
    organizations = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False, )
    online_lessons = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    offline_lessons = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    lessons_at_home = models.CharField(max_length=100, choices=CHOICES, default="+", null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    time_of_lesson = models.CharField(choices=TIME, default="60", null=False, blank=False, max_length=100)
    add_information = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=100, choices=CURRENCY, default="BYN", null=False, blank=False)
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE)





