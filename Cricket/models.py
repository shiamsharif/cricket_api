from django.db import models


class Cricket(models.Model):
    team_name = models.CharField(max_length=256)
    total_player = models.IntegerField()
    vanue = models.CharField(max_length=256, null=True, blank=True)
    batter = models.IntegerField()
    bowler = models.IntegerField()
    wicket_kipper = models.IntegerField()
    captain_name = models.CharField(max_length=256)