from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class PatientForm(ModelForm):
    class Meta:
        model = Patients
        fields= '__all__'
        exclude =['user','Problem','description']



class Solutionform(ModelForm):
    class Meta:
        model = Solutions
        fields = ['Doctors','Patients','description','status']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

