# Generated by Django 4.0.4 on 2022-09-10 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('Created', models.DateTimeField(default=datetime.datetime(2022, 9, 10, 12, 21, 52, 138039))),
            ],
        ),
    ]
