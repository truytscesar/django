# Generated by Django 4.1.7 on 2023-02-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_deteriora', '0002_alter_mymodeldatehj_col3'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelDateHj2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
