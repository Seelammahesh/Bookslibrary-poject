# Generated by Django 4.0.4 on 2022-09-10 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookslibrary',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 12, 27, 58, 512928)),
        ),
    ]