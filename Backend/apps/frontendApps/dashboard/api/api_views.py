from rest_framework.viewsets import ModelViewSet

from apps.frontendApps.dashboard.models import (
    DashBoardMetaModel,
    BannerSectionModel
)

from apps.frontendApps.dashboard.api.serializers import (
    DashBoardMetaSerializer,
    BannerSectionSerializer,
    PaginationSerializer
)


class DashBoardMetaViewSet(ModelViewSet):
    queryset = DashBoardMetaModel.objects.all()
    serializer_class = DashBoardMetaSerializer
    pagination_class = PaginationSerializer


class BannerSectionViewSet(ModelViewSet):
    queryset = BannerSectionModel.objects.all()
    serializer_class = BannerSectionSerializer
    pagination_class = PaginationSerializer
