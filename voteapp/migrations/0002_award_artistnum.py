# Generated by Django 2.2.1 on 2020-05-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='artistNum',
            field=models.IntegerField(default=0),
        ),
    ]
