from django.db import models

class PlayerStats(models.Model):
    player_name = models.CharField(max_length=50)
    total_matches = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    win_ratio = models.FloatField(default=0.0)
    ranking = models.IntegerField(default=0)
    
    