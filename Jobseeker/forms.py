from django import forms
from Jobseeker.models import JobseekerProfile
from django.forms import ModelForm


class JobseekerProfileForm(forms.ModelForm):
    class Meta:
        model=JobseekerProfile
        fields=["username","DOB","qualification","skills","experience","cv"]
        widgets = {
            "DOB": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "skills": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.NumberInput(attrs={"class": "form-control"}),
            }