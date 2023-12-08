from django.forms import ModelForm
from Employer.models import CompanyProfile,Jobs
from Jobseeker.models import Applications
from django import forms
from Employer.admin import UserCreationForm
from Employer.models import MyUser
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class EmpSignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    options = (("jobseeker", "jobseeker"),
               ("employer", "employer"))
    role= forms.ChoiceField(choices=options)
    class Meta:
        model=MyUser
        fields=['email','password1','password2','phone','role']
        widgets={
                    "phone":forms.NumberInput(attrs={"class":"form-control"}),
                    "email":forms.EmailInput(attrs={"class":"form-control"})

                }
        

class EmpLoginForm(forms.Form):
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise ValidationError("Invalid Email Address or Password")
        

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model=CompanyProfile
        fields=["company_name","services","founded_date","website"]
        widgets = {
            "founded_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "services": forms.Textarea(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude =['company','create_date']
        
            
class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model=Applications
        fields=["Interview_Date"]
        widgets={
            "Interview_Date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
