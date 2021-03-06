from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['fullName','phoneNumber','password','profilePic']