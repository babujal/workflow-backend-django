from .models import WorkOrder
from rest_framework import viewsets, permissions
from .serializers import WorkOrderSerializers

class WorkOrderViewsSet(viewsets.ModelViewSet):
    queryset=WorkOrder.objects.all()
    serializer_class=WorkOrderSerializers
    permission_classes=[permissions.AllowAny]