from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer

from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание Пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """ Переопределение Создателя """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """ Просмотр списка Пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр подробностей Пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление Пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление Пользователя """
    queryset = User.objects.all()
