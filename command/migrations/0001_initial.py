# Generated by Django 3.1 on 2021-04-01 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PinModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6)])),
            ],
        ),
    ]
