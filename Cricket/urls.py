from rest_framework import routers
from Cricket import views


router = routers.DefaultRouter()
router.register(r'', views.CricketViewSet, basename='cricket')



urlpatterns = router.urls