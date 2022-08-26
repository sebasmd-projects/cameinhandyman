from rest_framework.viewsets import ModelViewSet

from apps.contactinfo.models import ContactInfoModel

from apps.contactinfo.api.serializers import ContactInfoSerializer
from apps.dynamicform.api.serializers import PaginationSerializer

class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfoModel.objects.all()
    serializer_class = ContactInfoSerializer
    pagination_class = PaginationSerializer