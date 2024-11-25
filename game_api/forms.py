from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# myapp/forms.py
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get("username_or_email")
        password = cleaned_data.get("password")

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                # Tentar autenticar com o email
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass

            if user is None:
                raise forms.ValidationError("Login inválido.")
            cleaned_data['user'] = user

        return cleaned_data
