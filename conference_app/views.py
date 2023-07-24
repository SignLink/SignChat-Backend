

# from .serializers import RegistrationSerializer, AccountSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

from dj_rest_auth.registration.views import RegisterView
from .serializers import UserProfileSerializer

# Create your views here.
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user



class UserRegisterView(RegisterView):
    serializer_class = UserProfileSerializer
    
