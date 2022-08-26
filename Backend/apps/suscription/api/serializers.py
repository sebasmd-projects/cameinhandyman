from rest_framework import serializers

from apps.suscription.models import SuscriptionModel

class SuscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuscriptionModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')
        extra_kwargs = {
            'email' : {'required': True},
        }