from rest_framework.routers import DefaultRouter

from apps.contactinfo.api.api_views import ContactInfoViewSet

router = DefaultRouter()

router.register(
    r'',
    ContactInfoViewSet,
    basename='contact-info'
)

urlpatterns = router.urls