from rest_framework.routers import DefaultRouter

from regions.views import RegionViewSet

router = DefaultRouter()
router.register(r'', RegionViewSet)

urlpatterns = router.urls
