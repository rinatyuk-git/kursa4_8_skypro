from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
# from habits.paginators import PagePaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):  # Присвоение привычке Создателя
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Просмотр списка привычек """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated | IsOwner,)
    # pagination_class = PagePaginator

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр подробностей привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated | IsOwner,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Обновление привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class PublishedHabitListAPIView(generics.ListAPIView):
    """ Просмотр списка публичных привычек """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    # pagination_class = PagePaginator

    def get_queryset(self):
        """ Подготовка списка публичных привычек """
        return Habit.objects.filter(is_published=True)
