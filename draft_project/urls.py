from api_app.urls import urlpatterns as api_urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(api_urls)),
    path('', admin.site.urls),
]
