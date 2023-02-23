# Generated by Django 4.1.7 on 2023-02-22 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_deteriora', '0004_remove_mymodeldate_col2_mymodeldate_col3'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelDateHj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col3', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='mymodeldate',
            name='col3',
        ),
        migrations.AddField(
            model_name='mymodeldate',
            name='col2',
            field=models.DateTimeField(default=9999),
            preserve_default=False,
        ),
    ]
