from .models import WorkOrder
from rest_framework import serializers

class WorkOrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=WorkOrder
        fields = '__all__'