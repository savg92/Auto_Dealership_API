from rest_framework import routers
from .views import DealerLocationViewSet, CarViewSet, VersionViewSet, FeatureViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'dealer-locations', DealerLocationViewSet)
router.register(r'cars', CarViewSet)
router.register(r'versions', VersionViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls