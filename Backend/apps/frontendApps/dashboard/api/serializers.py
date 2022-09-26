from rest_framework import serializers, pagination

from apps.frontendApps.dashboard.models import (
    DashBoardMetaModel,
    BannerSectionModel
)

class DashBoardMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashBoardMetaModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')
        
class BannerSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerSectionModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')
        
class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 200