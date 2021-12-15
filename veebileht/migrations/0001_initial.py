# Generated by Django 3.2.9 on 2021-11-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('starttime', models.IntegerField()),
                ('endtime', models.IntegerField()),
                ('description', models.TextField()),
                ('participants', models.IntegerField()),
            ],
        ),
    ]
