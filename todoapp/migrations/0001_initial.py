# Generated by Django 5.0.6 on 2024-06-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=100)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
