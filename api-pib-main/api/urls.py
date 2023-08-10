from django.contrib import admin
from django.urls import path, include 
from core.views import IndiceViewSet, PIBViewSet
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    #path('api-auth/', include('rest_framework.urls'))
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]
