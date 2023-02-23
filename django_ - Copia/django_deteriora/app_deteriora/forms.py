from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


'''login'''
class EmailPasswordForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

'''cadastro'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailPasswordSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(EmailPasswordSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

