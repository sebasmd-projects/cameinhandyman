from rest_framework.viewsets import ModelViewSet

from apps.frontendApps.dynamicform.models import (
    TVSizeModel,
    TVSurfaceModel,
    TVWallMountModel,
    TVHandleCordsModel,
    TVOtherInstallsModel,
    TVQuestionsModel,
    TVWallMountInstallationModel
)

from apps.frontendApps.dynamicform.api.serializers import (
    TVSizeSerializer,
    TVSurfaceSerializer,
    TVWallMountSerializer,
    TVHandleCordsSerializer,
    TVOtherInstallsSerializer,
    TVQuestionsSerializer,
    TVWallMountInstallationSerializer,
    PaginationSerializer
)


class TVSizeViewSet(ModelViewSet):
    queryset = TVSizeModel.objects.all()
    serializer_class = TVSizeSerializer
    pagination_class = PaginationSerializer


class TVSurfaceViewSet(ModelViewSet):
    queryset = TVSurfaceModel.objects.all()
    serializer_class = TVSurfaceSerializer
    pagination_class = PaginationSerializer


class TVWallMountViewSet(ModelViewSet):
    queryset = TVWallMountModel.objects.all()
    serializer_class = TVWallMountSerializer
    pagination_class = PaginationSerializer


class TVHandleCordsViewSet(ModelViewSet):
    queryset = TVHandleCordsModel.objects.all()
    serializer_class = TVHandleCordsSerializer
    pagination_class = PaginationSerializer


class TVOtherInstallsViewSet(ModelViewSet):
    queryset = TVOtherInstallsModel.objects.all()
    serializer_class = TVOtherInstallsSerializer
    pagination_class = PaginationSerializer


class TVQuestionsViewSet(ModelViewSet):
    queryset = TVQuestionsModel.objects.all()
    serializer_class = TVQuestionsSerializer
    pagination_class = PaginationSerializer


class TVWallMountInstallationViewSet(ModelViewSet):
    queryset = TVWallMountInstallationModel.objects.all()
    serializer_class = TVWallMountInstallationSerializer
    pagination_class = PaginationSerializer
