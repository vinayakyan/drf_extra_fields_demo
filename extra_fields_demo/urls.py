from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app1.views import ProfileViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
