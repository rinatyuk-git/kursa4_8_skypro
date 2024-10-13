from rest_framework import serializers

from habits.models import Habit
from rest_framework.serializers import ValidationError


class HabitSerializer(serializers.ModelSerializer):

    def validate_related_action(self, obj):
        """ Проверка связанных привычек """
        if obj and not obj.is_pleasant:
            raise ValidationError("В связанные привычки могут попадать только приятные привычки.")
        return obj

    def validate(self, data):
        """ Проверка привычек на: """
        #  связанная привычка
        related_action = data.get('related_action') or (self.instance and self.instance.related_action)
        #  вознаграждение
        prize_action = data.get('prize_action') or (self.instance and self.instance.prize_action)
        #  приятная привычка
        is_pleasant = data.get('is_pleasant') or (self.instance and self.instance.is_pleasant)
        if related_action and prize_action:
            """ добавление связанной привычки и вознаграждения одновременно """
            raise ValidationError("Невозможен одновременный выбор связанной привычки и вознаграждения.")
        if is_pleasant and (related_action or prize_action):
            """ наличие у приятной привычки связанной привычки и вознаграждения """
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
        return data

    class Meta:
        model = Habit
        fields = "__all__"
