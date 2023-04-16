from rest_framework import serializers
from .models import Address


class GenerateAddress(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["coin", "seed", "private_key", "public_key", "address"]
