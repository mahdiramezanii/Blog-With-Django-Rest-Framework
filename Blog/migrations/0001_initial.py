# Generated by Django 4.1 on 2022-09-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('discription', models.TextField()),
            ],
        ),
    ]
