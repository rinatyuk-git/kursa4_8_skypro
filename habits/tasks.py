from datetime import datetime, timedelta

import pytz
from celery import shared_task

from config import settings
from habits.services import send_tg_msg
from habits.models import Habit


@shared_task
def share_information():
    """ Подготовка к отправке уведомления в Телеграм """
    habits = Habit.objects.all()
    now = datetime.now(pytz.timezone(settings.TIME_ZONE))
    for habit in habits:
        if habit.owner.tg_chat_id:

            if not habit.action_datetime:
                action_datetime = datetime.combine(now.date(), habit.action_time)
                habit.action_datetime = pytz.timezone(settings.TIME_ZONE).localize(action_datetime)

                if habit.action_datetime < now:
                    habit.action_datetime += timedelta(days=1)
                habit.save()

            habit_start_time = habit.action_datetime.replace(second=0, microsecond=0)
            habit_time_now = now.replace(second=0, microsecond=0)

            if habit_start_time == habit_time_now:
                if habit.action:
                    message = (f'Обрати внимание - пора {habit.action}.'
                               f'Для этого есть замечательное место - {habit.action_place}.'
                               f'Время начала было установлено на {habit.action_time}')
                    send_tg_msg(
                        message,
                        habit.owner.tg_chat_id,
                    )
                    habit.action_datetime = now.replace(second=0, microsecond=0) + timedelta(days=habit.periodic)
                    habit.save()

    #  сообщение для выполнения привычки я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
    # message = (f'Обрати внимание - пора делать{habit.action}.',
    # f'Для этого есть замечательное место в {habit.action_place}.',
    # f'Время начала было установлено на {habit.action_time_for}')
    #  сообщение для выполнения приятной привычки
    # message = (f'А теперь настала пора для{habit.action}.',
    #            # f'Для этого есть замечательное место в {habit.action_place}.',
    #            # f'Время начала было установлено на {habit.action_time_for}')
    #  сообщение для выполнения связанной привычки
    #  сообщение для выполнения вознаграждения
