#
# REPLACE the entire contents of contacts/views.py with this
#

from django.shortcuts import render  # <-- The import for render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Contact
from .serializers import ContactSerializer, UserSerializer
from django.contrib.auth.models import User

# --- Your API Class-Based Views ---

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all() # <-- This was in your previous version
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return user.contacts.all()
        return Contact.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# --- Your New HTML Page Views ---

def backend_login_page(request):
    """Serves the backend's HTML login page."""
    return render(request, 'backend_auth/login.html')

def backend_register_page(request):
    """Serves the backend's HTML register page."""
    return render(request, 'backend_auth/register.html')