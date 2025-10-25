from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from contacts import views as contacts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- ADD THESE NEW PATHS FOR YOUR HTML PAGES ---
    path('backend-login/', contacts_views.backend_login_page, name='backend-login'),
    path('backend-register/', contacts_views.backend_register_page, name='backend-register'),
    # -----------------------------------------------

    # Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', contacts_views.UserCreateView.as_view(), name='register'),

    # Contacts API
    path('api/', include('contacts.urls')),
]
