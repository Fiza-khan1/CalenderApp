from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Events(models.Model):
    person=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    day=models.DateField()
    start_date=models.TimeField()
    end_date=models.TimeField(null=True,blank=True)
    notes=models.TextField()
    def __str__(self):
        return self.notes
    












# idgets = {
#             'guest_author': forms.TextInput(attrs={'class': 'form-control input'}),
#             'title': forms.TextInput(attrs={'class': 'form-control input'}),
#             'teaser': forms.Textarea(attrs={'class': 'form-control input'}),
#             'category': forms.Select(choices=categories, attrs={'class': 'form-control input'}),
#             'content': forms.Textarea(attrs={'class': 'form-control input'}),
#             'tags': forms.TextInput(attrs={'class': 'form-control input'}),
#             'is_pub wlished': forms.CheckboxInput(attrs={'class': 'form-control-input'})
#         }