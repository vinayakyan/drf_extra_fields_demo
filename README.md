This project demonstrate the use of drf_extra_field to encode images to base64 images
for that install the package drf_extra_fields

=====pip install drf_extra_fields=====

and drf_extra_fields needs some extra dependancies of psycopg2 so you will have to install that
dependancy too.

=====pip install psycopg2=====

once you have installed the dependancies then you need to import Base64ImageField in serializers.py

if your model is 

from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pro_pic = models.ImageField(upload_to="pro_pics", null= True, blank= True)
    email = models.EmailField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

then your serializer will be like this 

from rest_framework import serializers
from .models import Profile
from drf_extra_fields.fields import Base64ImageField


class ProfileSerializer(serializers.ModelSerializer):
    pro_pic = Base64ImageField(required=False)

    class Meta:
        model = Profile
        fields = "__all__"

