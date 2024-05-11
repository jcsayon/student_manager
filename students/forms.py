from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'course', 'gender', 'age']
        widgets = {
            'gender': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Assuming 'gender' is a choice field in your model with choices directly defined
        self.fields['gender'].empty_label = None


class FilterForm(forms.Form):
    full_name = forms.CharField(required=False, label='Search by Full Name')
    course = forms.ChoiceField(choices=[
        ('', 'Any'),
        ('BS-CS', 'BS-CS'),
        ('BS-DS', 'BS-DS'),
        ('BS-IT', 'BS-IT'),
        ('BS-IS', 'BS-IS'),
    ], required=False)
    gender = forms.ChoiceField(choices=[
        ('', 'Any'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ], required=False)
    age_min = forms.IntegerField(required=False, label='Minimum Age')
    age_max = forms.IntegerField(required=False, label='Maximum Age')
