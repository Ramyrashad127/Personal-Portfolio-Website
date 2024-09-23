from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Project

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username', 'autofocus': True, 'required': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control' , 'placeholder': 'Password', 'required': True})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'birth_date', 'address', 'email', 'phone', 'education', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': False}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': False}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'technology', 'link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Project Name',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Project Description'}),
            'technology': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Technology Used'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter GitHub Link', 'required': False}),
        }
