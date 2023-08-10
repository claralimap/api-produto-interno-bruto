from core.views import IndiceViewSet, PIBViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'indice', IndiceViewSet)
router.register(r'pib', PIBViewSet)
