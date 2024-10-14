from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.test")
        self.habit = Habit.objects.create(
            action="Habit9_Test1",
            action_place="Place_Habit9_Test1",
            periodic=4,
            action_duration="00:02:00",
            # is_published=False,
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse('habits:habit_create')
        data = {
            "action": "Habit9_Test1",
            "action_place": "Place_Habit9_Test1",
            "periodic": 4,
            "action_duration": "00:02:00",
            "is_published": True,
            "owner": self.user.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_habit_list(self):
        url = reverse('habits:habits_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': self.habit.pk,
                 'action_place': self.habit.action_place,
                 'action_time': self.habit.action_time,
                 'action': self.habit.action,
                 'periodic': self.habit.periodic,
                 'action_duration': self.habit.action_duration,
                 'prize_action': self.habit.prize_action,
                 'is_pleasant': self.habit.is_pleasant,
                 'is_published': self.habit.is_published,
                 'action_datetime': self.habit.action_datetime,
                 'owner': self.user.pk,
                 'related_action': self.habit.related_action,
                 }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    # def test_habit_published_list(self):
    #     url = reverse('habits:publhabits_list')
    #     response = self.client.get(url)
    #     data = response.json()
    #     result = {
    #         'count': 1,
    #         'next': None,
    #         'previous': None,
    #         'results': [
    #             {'id': self.habit.pk,
    #              'action_place': self.habit.action_place,
    #              'action_time': self.habit.action_time,
    #              'action': self.habit.action,
    #              'periodic': self.habit.periodic,
    #              'action_duration': self.habit.action_duration,
    #              'prize_action': self.habit.prize_action,
    #              'is_pleasant': self.habit.is_pleasant,
    #              'is_published': True,
    #              'action_datetime': self.habit.action_datetime,
    #              'owner': self.user.pk,
    #              'related_action': self.habit.related_action,
    #              }
    #         ]
    #     }
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         data, result
    #     )

    def test_habit_retrieve(self):
        url = reverse('habits:habit_detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('action'), self.habit.action
        )

    def test_habit_update(self):
        url = reverse('habits:habit_update', args=(self.habit.pk,))
        data = {
            "action": "Habit9_Test1",
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('action'), "Habit9_Test1"
        )

    def test_habit_delete(self):
        url = reverse('habits:habit_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )
