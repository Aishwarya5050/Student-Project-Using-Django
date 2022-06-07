from django import forms
from django.forms import fields
from student_App import models
from django import forms
from student_App.models import stud
 
class studentRegistration(forms.ModelForm):
    class Meta:
        model = stud
        fields = '__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model = stud
        fields = "__all__"
 