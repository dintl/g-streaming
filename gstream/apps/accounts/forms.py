
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Interest
from gstream.apps.locations.models import Country

class RegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    
    first_name = forms.CharField(label='First name', max_length=30)
    last_name  = forms.CharField(label='Last name', max_length=30)
    
    username  = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$',
    error_messages = {'invalid': "This value may contain only letters, numbers and the characters @.+-_ "})
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput,
    help_text = "Enter the same password as above, for verification.")
       
    email  = forms.EmailField(label="Email")
    country = forms.ModelChoiceField(queryset=Country.objects.all())

    interests = forms.ModelMultipleChoiceField(queryset=Interest.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    
    accept_terms_website = forms.BooleanField(label='I accept the G-Streaming Website Terms and Conditions.')
   
    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists.")
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("A user with that email already exists.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all())

    class Meta:
        model = Profile
