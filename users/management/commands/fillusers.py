from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user_list = [
            {'email': 'user1@mail.info',
             'password': 'User1_1resU',
             'phone': '+659823685',
             'city': 'Chicago'},
            {'email': 'user2@mail.info',
             'password': 'User2_2resU',
             'phone': '+9584624180',
             'city': 'Xin'},
            {'email': 'user3@mail.info',
             'password': 'user3_3resu',
             'phone': '+9854823668',
             'city': 'Tokio'},
        ]
        users_for_create = []
        for item in user_list:
            users_for_create.append(
                User(**item)
            )

        User.objects.bulk_create(users_for_create)

# python manage.py fillusers
