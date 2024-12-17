from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=500)
    phone_number = serializers.CharField(max_length=15)
    next_of_kin = serializers.CharField(max_length=255)
    next_of_kin_phone = serializers.CharField(max_length=15)
    dnr_status = serializers.BooleanField(default=False)  # Assuming it's a boolean
    nfc_tag = serializers.BooleanField(default=False)  # Assuming it's a boolean
