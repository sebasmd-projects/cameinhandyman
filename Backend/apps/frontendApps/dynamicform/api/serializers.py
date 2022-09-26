from rest_framework import serializers, pagination

from apps.frontendApps.dynamicform.models import (
    TVSizeModel,
    TVSurfaceModel,
    TVWallMountModel,
    TVHandleCordsModel,
    TVOtherInstallsModel,
    TVQuestionsModel,
    TVWallMountInstallationModel
)


class TVSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVSizeModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVSurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVSurfaceModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVWallMountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVWallMountModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVHandleCordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVHandleCordsModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVOtherInstallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVOtherInstallsModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVQuestionsModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class TVWallMountInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVWallMountInstallationModel
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 200
