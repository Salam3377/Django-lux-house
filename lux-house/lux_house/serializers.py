from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models.menu import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        field = '__all__'
        model = Menu