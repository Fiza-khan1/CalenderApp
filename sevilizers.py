from rest_framework import  serializers
from .models import Events
from django.contrib.auth.models import User

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        # fields=['person', 'day','start_date','notes']
        exclude=['end_date']

        


