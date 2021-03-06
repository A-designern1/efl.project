# Generated by Django 4.0.2 on 2022-05-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('quantity_of_teams', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('quantity_of_players', models.IntegerField(max_length=30)),
                ('victories', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('secondName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
