from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


# Create your tests here.
class HabitsTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro")
        self.user.set_password('admin')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="дома",
            # time="08:05:00",
            action="выпить стакан воды",
            is_pleasant=False,
            period=1440,
            duration=timedelta(minutes=1),
            reward="погладить кошку",
            is_public=True,
            related_habit=None,
        )

    def test_habit_create(self):
        """Тест создания привычки"""
        url = reverse('habits:habits-create')
        data = {'owner': self.user.id,
                'place': "дома",
                # 'time': "08:40:00",
                'action': "съесть кашу на завтрак",
                'is_pleasant': False,
                'period': 4320,
                'duration': timedelta(minutes=2),
                'reward ': "выпить кофе",
                'is_public': True,
                }
        response = self.client.post(url, data=data)
        print('\ntest_habit_create')
        print(response.json())
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_retrieve(self):
        """Тест получения привычки"""
        url = reverse('habits:habits-get', kwargs={'pk': self.habit.id})
        response = self.client.get(url)
        print('\ntest_habits_retrieve')
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        """Тестирование изменения привычки"""
        url = reverse('habits:habits-update', kwargs={'pk': self.habit.id})
        new_data = {
            "reward": "послушать любимую песню",
        }
        response = self.client.patch(url, data=new_data)
        print('\ntest_habit_update')
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), 'послушать любимую песню')

    def test_habit_delete(self):
        """Тестирование удаления привычки"""
        url = reverse('habits:habits-delete', kwargs={'pk': self.habit.id})
        response = self.client.delete(url)
        print('\ntest_habit_delete')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тестирование вывода списка привычек"""
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        print('\ntest_habit_list')
        print(response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
