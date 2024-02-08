from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serialazers.bonus import SerializersBonus
from .services.User_bonus_constructor import UserBonusConstructor
from .services.bonus_programs.program_type import Programs


class CreateBonusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={201: SerializersBonus},
    )
    def get(self, request):
        """create random bonus for user"""
        try:
            program_name = Programs.random_bonus.name
            bonus_constructor = UserBonusConstructor(user=request.user, bonus_name=program_name)
            user_bonuses = [user_bonus.bonus for user_bonus in bonus_constructor.add_user_bonus()]
            return Response(SerializersBonus(user_bonuses, many=True).data)
        except (ValueError, KeyError) as ex:
            return Response(
                {
                    "status_code": 400,
                    "default_detail": str(ex),
                    "default_code": 400
                },
                status=status.HTTP_400_BAD_REQUEST
            )
