# views.py
from auth_app.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():

            # Check if user already exists
            user = User.objects.filter(email=serializer.validated_data["email"]).first()
            if user is not None:
                return Response(
                    {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
                )

            # Create user
            user = User.objects.create(
                first_name=serializer.validated_data["first_name"],
                last_name=serializer.validated_data["last_name"],
                email=serializer.validated_data["email"],
            )
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response(
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = User.objects.filter(email=email).first()
            if user is None:
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
            if not user.check_password(password):
                return Response(
                    {"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST
                )
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            data={"message": "You have accessed a protected view!"},
            status=status.HTTP_200_OK,
        )
    
class UserListView(APIView):
    permission_classes = [IsAuthenticated,IsSuperUser ]  # Ensure the user is authenticated to access this view

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
