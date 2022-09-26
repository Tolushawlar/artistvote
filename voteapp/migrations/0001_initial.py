# Generated by Django 2.2.1 on 2020-05-18 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(blank=True, max_length=200, null=True)),
                ('votes', models.IntegerField(default=0)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='voteapp.Award')),
            ],
        ),
    ]