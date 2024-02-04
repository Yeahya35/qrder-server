from django.urls import path
from .token import *
from .views import *

urlpatterns = [
    path("auth/login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/set-csrf-cookie", set_csrf_token, name="logout"),
    path("auth/refresh", RefreshViewSet.as_view(), name="token_refresh"),
    path("auth/register", register, name="register"),
]
