from rest_framework.routers import DefaultRouter

from apps.frontendApps.dynamicform.api.api_views import (
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
    r'form-size',
    TVSizeViewSet,
    basename="form-size"
)

router.register(
    r'form-surface',
    TVSurfaceViewSet,
    basename="form-surface"
)

router.register(
    r'form-wall-mount',
    TVWallMountViewSet,
    basename="form-wall-mount"
)

router.register(
    r'form-handle-cords',
    TVHandleCordsViewSet,
    basename="form-handle-cords"
)

router.register(
    r'forms-other-installs',
    TVOtherInstallsViewSet,
    basename="forms-other-installs"
)

router.register(
    r'forms-questions',
    TVQuestionsViewSet,
    basename="forms-questions"
)

router.register(
    r'forms-dynamic-form',
    TVWallMountInstallationViewSet,
    basename="forms-dynamic-form"
)

urlpatterns = router.urls
