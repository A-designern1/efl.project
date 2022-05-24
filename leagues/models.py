from django.db import models


# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=20)
    secondName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstName + ' ' + self.secondName


class Team(models.Model):
    team_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    quantity_of_players = models.IntegerField(max_length=30)
    victories = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name + ' ' + self.description


class League(models.Model):
    league_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    quantity_of_teams = models.IntegerField(max_length=30)


    def __str__(self):
        return self.league_name
