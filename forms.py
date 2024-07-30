from django import forms 
from .models import Events
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class EventForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for myField in self.fields:
             self.fields[myField].widget.attrs['class'] = 'form-control'
            
        
    class Meta:
        model = Events 
        exclude={'person'}
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.TimeInput(attrs={'type': 'time'}),
            'end_date': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'day': 'Date',
            'start_date': 'Start Time',
            'end_date': 'End Time',
            'notes': 'Event Notes'
        }


class sign_up(UserCreationForm):   
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for myField in self.fields:
             self.fields[myField].widget.attrs['class'] = 'form-control'      
    class Meta:   
        model = User 
        fields=['username','first_name','last_name','email','password1','password2']

       

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for myField in self.fields:
             self.fields[myField].widget.attrs['class'] = 'form-control'  
    
