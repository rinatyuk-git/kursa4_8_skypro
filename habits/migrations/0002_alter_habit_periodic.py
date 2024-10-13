# Generated by Django 5.1.2 on 2024-10-11 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodic',
            field=models.SmallIntegerField(blank=True, default=1, help_text='Укажите периодичность выполнения привычки в днях', null=True, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='Периодичность'),
        ),
    ]