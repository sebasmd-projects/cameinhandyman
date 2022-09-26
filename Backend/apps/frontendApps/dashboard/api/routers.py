from rest_framework.routers import DefaultRouter

from apps.frontendApps.dashboard.api.api_views import (
    DashBoardMetaViewSet,
    BannerSectionViewSet
)

router = DefaultRouter()

router.register(
    r'meta-tags',
    DashBoardMetaViewSet,
    basename="meta-tags"
)

router.register(
    r'banner-section',
    BannerSectionViewSet,
    basename="banner-section"
)

urlpatterns = router.urls
