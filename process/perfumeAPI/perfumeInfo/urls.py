from rest_framework import routers
from .views import perfumeInfoViewSet

router = routers.DefaultRouter()
router.register(r'perfume_info', perfumeInfoViewSet)

urlpatterns = router.urls
