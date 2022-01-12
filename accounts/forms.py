from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Password',
            'id': 'password',
        }
    ))


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Password',
            }
        )

        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Confirm password',
            }
        )
