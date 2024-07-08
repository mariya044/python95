from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponse
from user.models import NewUser


class UserRegisterForm(forms.ModelForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())
    username = forms.CharField(label='username')
    email = forms.CharField(label='email')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', "email", "first_name", "last_name", "password","groups"]

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            return HttpResponse('This email is already exists')
        return email

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

