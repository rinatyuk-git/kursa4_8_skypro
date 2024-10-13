from datetime import timedelta

from django.db import models
from django.core.validators import MaxValueValidator
from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель",
        help_text="Укажите Создателя привычки",
        **NULLABLE,
    )  # Пользователь — создатель привычки.
    action_place = models.CharField(
        max_length=155,
        verbose_name="Место действия",
        help_text="Укажите место действия",
        **NULLABLE,
    )  # Место — место, в котором необходимо выполнять привычку.
    action_time = models.TimeField(
        verbose_name='Время начала выполнения привычки',
        help_text="Укажите время, когда необходимо выполнять привычку",
        ** NULLABLE,
    )  # Время — время, когда необходимо выполнять привычку.
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        help_text="Действие, которое представляет собой привычка",
        ** NULLABLE,
    )  # Действие — действие, которое представляет собой привычка.
    periodic = models.SmallIntegerField(
        verbose_name='Периодичность',
        help_text="Укажите периодичность выполнения привычки в днях",
        default=1,
        validators=[MaxValueValidator(7)],
        **NULLABLE,
    )  # Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
    action_duration = models.DurationField(
        verbose_name='Продолжительность',
        help_text="Укажите продолжительность выполнения привычки в минутах",
        default=timedelta(minutes=2),
        validators=[MaxValueValidator(timedelta(minutes=2))],
        **NULLABLE,
    )  # Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
    related_action = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        **NULLABLE,
    )  # Связанная привычка — привычка, которая связана с другой привычкой,
    # важно указывать для полезных привычек, но не для приятных.
    prize_action = models.CharField(
        max_length=255,
        verbose_name="Вознаграждение",
        help_text="Действие, которое представляет собой вознаграждение",
        ** NULLABLE,
    )  # Вознаграждение — чем пользователь должен себя вознаградить после выполнения привычки.
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки',
    )  # Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    is_published = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
    )  # Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в
    # пример чужие привычки.
    action_datetime = models.DateTimeField(
        verbose_name='Дата/Время циклического выполнения привычки',
        help_text="Укажите время, когда необходимо выполнять привычку",
        **NULLABLE,
    )  # Дата/Время — дата/время, когда запускается цикличность привычек.

    def __str__(self):
        return f'я буду {self.action} в {self.action_time} в {self.action_place}'
    # я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
