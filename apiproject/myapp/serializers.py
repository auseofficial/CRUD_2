from rest_framework import serializers
from myapp.models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'title', 'email']
