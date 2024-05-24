from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, MyHabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView


app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habits-list'),
    path('my_habits/', MyHabitListAPIView.as_view(), name='my-habits-list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits-get'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habits-delete')
]
