from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .containers import container
from .serialazers.bonus import SerializersBonus
from .services.bonuses.random_bonus import RandomBonus


class CreateRandomBonusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={201: SerializersBonus},
    )
    def get(self, request):
        """create random bonus for user"""
        try:
            random_bonus = container.resolve(RandomBonus)
            created_bonus = random_bonus.add_user_bonus(user=request.user)
            return Response(SerializersBonus(created_bonus.bonus).data)
        except (ValueError, KeyError) as ex:
            return Response(
                {
                    "status_code": 400,
                    "default_detail": str(ex),
                    "default_code": 400
                },
                status=status.HTTP_400_BAD_REQUEST
            )
