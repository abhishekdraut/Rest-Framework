from django.db.models.fields import DateTimeField
from rest_framework import serializers,routers
from rest_framework.fields import DateField


class blogseri(serializers.Serializer):

    title1 = serializers.CharField(max_length=10)
    description1=serializers.CharField(max_length=20)
    
    date1=DateField()

