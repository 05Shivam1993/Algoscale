from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border'}))
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    # def clean(self):
    #     super(SignUpForm, self).clean()
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     email = self.cleaned_data.get('email')
    #     first_name = self.cleaned_data.get('first_name')
    #     last_name = self.cleaned_data.get('last_name')
    #     if not username:
    #         self._errors['username'] = self.error_class([
    #             'Please provide your username'])
    #     if not email:
    #         self._errors['email'] = self.error_class([
    #             'Please provide your email'])
    #     if not password:
    #         self._errors['password'] = self.error_class([
    #             'Please provide password'])
    #     if not first_name:
    #         self._errors['first_name'] = self.error_class([
    #             'Please provide your first_name'])
    #     if not last_name:
    #         self._errors['last_name'] = self.error_class([
    #             'Please provide your last_name'])
    #     return self.cleaned_data
