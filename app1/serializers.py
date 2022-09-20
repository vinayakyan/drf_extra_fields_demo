from rest_framework import serializers
from .models import Profile
from drf_extra_fields.fields import Base64ImageField


class ProfileSerializer(serializers.ModelSerializer):
    pro_pic = Base64ImageField(required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'pro_pic', 'full_name']