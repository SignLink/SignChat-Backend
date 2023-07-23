from django.shortcuts import render
from .models import Account
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .serializers import RegistrationSerializer, AccountSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Create your views here.
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user

class RegistrationView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegistrationSerializer

class AccountDetailsView(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
