from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)
    class Meta:
        model = User
        fields =('first_name','last_name', 'email')
    # can use def clean_<any field name> to clean the value or raise validation errors
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        approved_emails = ["@goldfieldsmoney.com.au","@betterchoice.com.au","@finsure.com.au","@bnk.com.au"]
        cd = self.cleaned_data
        submitted_email = cd.get('email')
        email_used = User.objects.filter(email = submitted_email).count()
        checked_domain = [x for x in approved_emails if x in submitted_email]
        if len(checked_domain)==0:
            raise forms.ValidationError('Please only use emails from approved domains.')
        if email_used:
            raise forms.ValidationError('This email has been used to register for another account.')
        return cd['email']
