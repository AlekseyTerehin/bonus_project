from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='regis'),
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
