from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]