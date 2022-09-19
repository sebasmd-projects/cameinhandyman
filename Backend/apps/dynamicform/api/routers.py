from rest_framework.routers import DefaultRouter

from apps.dynamicform.api.api_views import (
    TVSizeViewSet,
    TVSurfaceViewSet,
    TVWallMountViewSet,
    TVHandleCordsViewSet,
    TVOtherInstallsViewSet,
    TVQuestionsViewSet,
    TVWallMountInstallationViewSet,
)

router = DefaultRouter()

router.register(
    r'dynamicform/form-size',
    TVSizeViewSet,
    basename="form-size"
)

router.register(
    r'dynamicform/form-surface',
    TVSurfaceViewSet,
    basename="form-surface"
)

router.register(
    r'dynamicform/form-wall-mount',
    TVWallMountViewSet,
    basename="form-wall-mount"
)

router.register(
    r'dynamicform/form-handle-cords',
    TVHandleCordsViewSet,
    basename="form-handle-cords"
)

router.register(
    r'dynamicform/forms-other-installs',
    TVOtherInstallsViewSet,
    basename="forms-other-installs"
)

router.register(
    r'dynamicform/forms-questions',
    TVQuestionsViewSet,
    basename="forms-questions"
)

router.register(
    r'dynamicform/forms-dynamic-form',
    TVWallMountInstallationViewSet,
    basename="forms-dynamic-form"
)

urlpatterns = router.urls
