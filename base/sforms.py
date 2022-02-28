from unittest.util import _MAX_LENGTH
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'input class':'input', 'type':'text', 'placeholder':'John'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'input class':'input', 'type':'text', 'placeholder':'Doe'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'input class':'input', 'type':'text', 'placeholder':'johndoe@email.com'}))
    phone_Number = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'input class':'input', 'type':'number', 'placeholder':'306-955-9555'}))
    #username = 

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_Number', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['input class'] = 'input'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['username'].widget.attrs['placeholder'] = 'username'

        self.fields['password1'].widget.attrs['input class'] = 'input'
        self.fields['password1'].widget.attrs['type'] = 'text'
        self.fields['password1'].widget.attrs['placeholder'] = '*****'


        self.fields['password2'].widget.attrs['input class'] = 'input'
        self.fields['password2'].widget.attrs['type'] = 'text'
        self.fields['password2'].widget.attrs['placeholder'] = '*****'


        for fieldname in ['password1']:
            self.fields[fieldname].label = 'Password'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
