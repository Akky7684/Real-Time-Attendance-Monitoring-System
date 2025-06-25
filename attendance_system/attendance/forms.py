from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    aruco_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profile = UserProfile(user=user, aruco_id=self.cleaned_data['aruco_id'])
            profile.save()
        return user