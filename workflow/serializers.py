from .models import WorkOrder
from rest_framework import serializers
from django.contrib.auth.models import User

class WorkOrderSerializers(serializers.HyperlinkedModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=WorkOrder
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username', 'password'] #We can add 'email here then specify it below in user if we want to include that field
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'], #In this case you can use braets['username'] or parenticis('username'), it does not matter
            password=validated_data['password']
        )
        return user






