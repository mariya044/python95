from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    ROLE=(
        ('student',"student"),
        ('teacher',"teacher"),
    )
    username=models.CharField(max_length=100, null=False, blank=False,unique=True)
    email = models.EmailField(unique=True, max_length=110,null=False, blank=False)
    password=models.CharField(max_length=100,null=False, blank=False)
    phone = models.CharField(max_length=14, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    role=models.CharField(choices=ROLE,default="student",max_length=20)


    def __str__(self):
        return self.email


from django.db import models

# Create your models here.
