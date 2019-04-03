from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from .models import User
from .serializers import UserListSerializer, UserDetailSerializer


class UserListCreateAPIView(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserListSerializer
	permission_classes = [AllowAny]


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserDetailSerializer
	permission_classes = [IsAdminUser]