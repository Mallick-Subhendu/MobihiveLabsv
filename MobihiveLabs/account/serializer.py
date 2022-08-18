from rest_framework import serializers
from .models import Profile

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','address','city','phone','date_of_birth','photo']