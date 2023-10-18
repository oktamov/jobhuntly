from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserLoginSerializer, UserPasswordChangeSerializer, UserRegisterSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserRegisterSerializer


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import UserLoginSerializer


class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()  # Make sure to import User

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            tokens = serializer.validated_data['tokens']

            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    # Add other user fields if you want.
                },
                'tokens': tokens
            }, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)


class UserLogoutView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"detail": "Logged out successfully."})


class UserPasswordChangeView(generics.GenericAPIView):
    serializer_class = UserPasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        return Response({"detail": "successfully password change"})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def put(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
