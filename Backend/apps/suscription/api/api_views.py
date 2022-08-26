from rest_framework.viewsets import ModelViewSet

from apps.dynamicform.api.serializers import PaginationSerializer

from apps.suscription.models import SuscriptionModel

from apps.suscription.api.serializers import SuscriptionSerializer

class SuscriptionViewSet(ModelViewSet):
    queryset = SuscriptionModel.objects.all()
    serializer_class = SuscriptionSerializer
    pagination_class = PaginationSerializer