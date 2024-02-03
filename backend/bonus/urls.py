from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/user_bonus_create', views.CreateBonusAPIView().as_view())
]
