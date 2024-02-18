from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repositories.user_queries import UserQueries
from .serializers.register import RegisterUserSerializer
from .serializers.users import SerializersUsers


class UserRegister(APIView):

    permission_classes = [AllowAny]

    @extend_schema(
        request=RegisterUserSerializer,
        responses={201: RegisterUserSerializer},
    )
    def post(self, request):
        """Registration user"""
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"User": serializer.data})
        return Response({"errors": serializer.errors})


class UsersAPIView(generics.ListAPIView):
    """All users"""

    serializer_class = SerializersUsers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserQueries().get_users()
