from dataclasses import fields
from pyexpat import model
from .models import BookModel
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

