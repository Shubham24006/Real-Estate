from .models import Profile
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={}),
        required=True, max_length=30
    )
    email = forms.CharField(
        required=True
    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'is_seller', 'description'
                            , 'photo']

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     if len(phone_number) < 10:
    #         raise forms.ValidationError('Phone Number not be less then 10 digits.')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        email = user.email
        phone_number = user.phone_number
        if len(phone_number) < 10:
            forms.ValidationError('Phone Number must not be less then 10 digits.')
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('please write valid email address')
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'description', 'photo']

    def save(self, commit=True):
        user = super(UpdateProfileForm, self).save(commit=False)
        email = user.email
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('please write valid email address to update user')
        if commit:
            user.save()
        return user

    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')
    #
    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = Profile.objects.get(email=email)
    #     except Profile.DoesNotExist:
    #         # Unable to find a user, this is fine
    #         return email
    #
    #     # A user was found with this as a username, raise an error.
    #     raise forms.ValidationError('This email address is already in use.')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
