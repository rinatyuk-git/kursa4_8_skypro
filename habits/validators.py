from datetime import timedelta

from rest_framework.serializers import ValidationError

from habits.models import Habit

# todo
def validate_relation(value):
    obj = Habit.objects.get(id=value)
    if not obj.is_pleasant:
        raise ValidationError("В связанные привычки могут попадать только пприятные привычки.")
    return value



# todo
class DurationValidator:

    def __init__(self, action_duration):
        self.action_duration = action_duration

    def __call__(self, habit):
        """ Проверка времени выполнения дейставия, должно быть не больше 120 секунд. """
        max_duration = timedelta(minutes=2),
        print(max_duration)
        tmp_duration = dict(habit).get(self.action_duration)
        print(tmp_duration)
        if tmp_duration > max_duration:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class RelatioValidator:

    def __init__(self, action_duration):
        self.action_duration = action_duration

