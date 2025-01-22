from django.urls import path, include
from .views import ItemViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('item', ItemViewset)

urlpatterns = [
    path('', include(router.urls)),
]+router.urls
