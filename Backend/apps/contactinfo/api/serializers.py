from rest_framework import serializers

from apps.contactinfo.models import ContactInfoModel

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfoModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')
        extra_kwargs = {
            'celPhone': {'required': True},
            'email': {'required': True},
        }