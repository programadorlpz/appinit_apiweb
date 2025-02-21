from django.db import models

class Player(models.Model):
    nombre = models.CharField(max_length=50)

class Game(models.Model):
    jugador1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='jugador1')
    jugador2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='jugador2')
    ronda_actual = models.IntegerField(default=1)
    ganador = models.CharField(max_length=50, null=True, blank=True)

class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    numero_ronda = models.IntegerField()
    ganador_ronda = models.CharField(max_length=50, null=True, blank=True)
    movimiento_j1 = models.CharField(max_length=10, null=True, blank=True)
    movimiento_j2 = models.CharField(max_length=10, null=True, blank=True)
