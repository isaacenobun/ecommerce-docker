from rest_framework import viewsets

from .models import item
from .serializers import itemSerializer

# Create your views here.

class ItemViewset(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = itemSerializer