from rest_framework.routers import DefaultRouter

from continents.views import ContinentViewSet

router = DefaultRouter()
router.register(r'', ContinentViewSet)

urlpatterns = router.urls
