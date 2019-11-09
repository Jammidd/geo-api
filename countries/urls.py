from rest_framework.routers import DefaultRouter

from countries.views import CountryViewSet

router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = router.urls
