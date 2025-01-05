from .models import WorkOrder
from rest_framework import viewsets, status
from .serializers import WorkOrderSerializers, UserSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class WorkOrderViewsSet(viewsets.ModelViewSet):
    queryset=WorkOrder.objects.all()
    serializer_class=WorkOrderSerializers
    # permission_classes=[permissions.AllowAny]
    permission_classes=[IsAuthenticated]
    # automaticaly associate the workorder with the authenticated user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #  only return workorders created by the authenticated user
    def get_queryset(self):
        return WorkOrder.objects.filter(user=self.request.user)


# THis querry returns all workorders in even if doesn't belong to the user
# Changes were necesary in views.py and urls.py.
# in urls.py was necesary to add to the registration of the route basename the basename specifyed.
class AdminWorkOrderViewsSet(viewsets.ModelViewSet):
    queryset=WorkOrder.objects.all()
    serializer_class=WorkOrderSerializers

    def get_queryset(self):
        return super().get_queryset()

class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            