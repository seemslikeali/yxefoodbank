from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


# Setting paramaters for account registrations
class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'username', 'password1', 'password2', )


# To check a valid account for login with Django Account form
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
