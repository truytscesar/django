# Generated by Django 4.1.7 on 2023-02-22 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelDateHj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col3', models.DateTimeField(verbose_name=datetime.date(2023, 2, 22))),
            ],
        ),
    ]
