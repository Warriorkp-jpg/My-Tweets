from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': "form-control",
            'placeholder': "Enter your tweet here"
        })
        self.fields['image'].widget.attrs.update({
            'class': "form-control"
        })

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
   class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})