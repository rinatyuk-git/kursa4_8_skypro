from celery import shared_task

from habits.services import send_tg_msg
from habits.models import Habit


@shared_task
def share_information():
    """ Подготовка к отправке уведомления в Телеграм """
    message = "Message1"
    updated_habit = Habit.objects.all()
    for item in updated_habit:
    # user = User.objects.all()
        if item.owner.tg_chat_id:
            send_tg_msg(message, item.owner.tg_chat_id)
