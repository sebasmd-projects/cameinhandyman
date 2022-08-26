from rest_framework.routers import DefaultRouter

from apps.suscription.api.api_views import SuscriptionViewSet

router = DefaultRouter()

router.register(
    r'',
    SuscriptionViewSet,
    basename='suscription'
)

urlpatterns = router.urls