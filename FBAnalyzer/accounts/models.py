# This is the file where Django backend models = database tables are created

from django.db import models
import uuid

# Create your models here

class Level(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    isSenior = models.BooleanField()
    isMale = models.BooleanField()

    def __str__(self):
        return f'{self.name}, {self.country}'

class Team(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    isNational = models.BooleanField()
    'l1c = models.ManyToManyField("Player", null=True)'
    'l1lw = models.ManyToManyField("Player", null=True)'
    'l1rw = models.ManyToManyField("Player", null=True)'
    'l1ld = models.ManyToManyField("Player", null=True)'
    'l1rd = models.ManyToManyField("Player", null=True)'
    'l2c = models.ManyToManyField("Player", null=True)'
    'l2lw = models.ManyToManyField("Player", null=True)'
    'l2rw = models.ManyToManyField("Player", null=True)'
    'l2ld = models.ManyToManyField("Player", null=True)'
    'l2rd = models.ManyToManyField("Player", null=True)'
    'l3c = models.ManyToManyField("Player", null=True)'
    'l3lw = models.ManyToManyField("Player", null=True)'
    'l3rw = models.ManyToManyField("Player", null=True)'
    'l3rd = models.ManyToManyField("Player", null=True)'
    'goalie = models.ManyToManyField("Player", null=True)'

    def __str__(self):
        return f'{self.name}, {self.level}'

class Player(models.Model):
    objects = models.Manager()

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    jersey_number = models.IntegerField()
    team = models.ManyToManyField(Team, null=True)
    'nationalTeam = models.ManyToManyField(Team, null=True)'

    def __str__(self):
        """String for representing the Model object."""
        return f'#{self.jersey_number} {self.first_name} {self.last_name}'

class Shot(models.Model):
    objects = models.Manager()

    time = models.IntegerField()
    'shooter = models.ManyToManyField(Player, null=True)'
    'passer = models.ManyToManyField(Player, null=True)'
    type = models.IntegerField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    angle = models.DecimalField(max_digits=5, decimal_places=2)
    xG = models.DecimalField(max_digits=5, decimal_places=2)
    isPP = models.BooleanField()
    isSH = models.BooleanField()

    """ Players on field sf = shot for , sa = shot against """
    'sfc = models.ManyToManyField(Player, null=True)'
    'sflw = models.ManyToManyField(Player, null=True)'
    'sfrw = models.ManyToManyField(Player, null=True)'
    'sfld = models.ManyToManyField(Player, null=True)'
    'sfrd = models.ManyToManyField(Player, null=True)'
    'sac = models.ManyToManyField(Player, null=True)'
    'salw = models.ManyToManyField(Player, null=True)'
    'sarw = models.ManyToManyField(Player, null=True)'
    'sald = models.ManyToManyField(Player, null=True)'
    'sard = models.ManyToManyField(Player, null=True)'
    'sag = models.ManyToManyField(Player, null=True)'''

    def __str__(self):
        return f'{self.type}, {self.result}'

class Game(models.Model):
    objects = models.Manager()
    
    # Game variables
    date = models.DateTimeField(auto_now=True, blank=True)
    periodNr = models.IntegerField(null=True)
    gameClock = models.IntegerField(null=True)
    periodClock = models.IntegerField(null=True)
    
    # Team variables
    nameT1 = models.CharField(max_length=50, null=True)
    lineOnT1 = models.IntegerField(null=True)
    possessionPeriodT1 = models.IntegerField(null=True)
    possessionGameT1 = models.IntegerField(null=True)
    goalsPeriodT1 = models.IntegerField(null=True)
    goalsGameT1 = models.IntegerField(null=True)
    xGPeriodT1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGGameT1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    nameT2 = models.CharField(max_length=50, null=True)
    lineOnT2 = models.IntegerField(null=True)
    possessionPeriodT2 = models.IntegerField(null=True)
    possessionGameT2 = models.IntegerField(null=True)
    goalsPeriodT2 = models.IntegerField(null=True)
    goalsGameT2 = models.IntegerField(null=True)
    xGPeriodT2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGGameT2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    
    # Line variables
    nameL1 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L1 = models.IntegerField(null=True)
    possessionGameT1L1 = models.IntegerField(null=True)
    gfPeriodT1L1 = models.IntegerField(null=True)
    gfGameT1L1 = models.IntegerField(null=True)
    gaPeriodT1L1 = models.IntegerField(null=True)
    gaGameT1L1 = models.IntegerField(null=True)
    TOCPeriodT1L1 = models.IntegerField(null=True)
    TOCGameT1L1 = models.IntegerField(null=True)
    xGfPeriodT1L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L1 = models.IntegerField(null=True)
    possessionGameT2L1 = models.IntegerField(null=True)
    gfPeriodT2L1 = models.IntegerField(null=True)
    gfGameT2L1 = models.IntegerField(null=True)
    gaPeriodT2L1 = models.IntegerField(null=True)
    gaGameT2L1 = models.IntegerField(null=True)
    TOCPeriodT2L1 = models.IntegerField(null=True)
    TOCGameT2L1 = models.IntegerField(null=True)
    xGfPeriodT2L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL2 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L2 = models.IntegerField(null=True)
    possessionGameT1L2 = models.IntegerField(null=True)
    gfPeriodT1L2 = models.IntegerField(null=True)
    gfGameT1L2 = models.IntegerField(null=True)
    gaPeriodT1L2 = models.IntegerField(null=True)
    gaGameT1L2 = models.IntegerField(null=True)
    TOCPeriodT1L2 = models.IntegerField(null=True)
    TOCGameT1L2 = models.IntegerField(null=True)
    xGfPeriodT1L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L2 = models.IntegerField(null=True)
    possessionGameT2L2 = models.IntegerField(null=True)
    gfPeriodT2L2 = models.IntegerField(null=True)
    gfGameT2L2 = models.IntegerField(null=True)
    gaPeriodT2L2 = models.IntegerField(null=True)
    gaGameT2L2 = models.IntegerField(null=True)
    TOCPeriodT2L2 = models.IntegerField(null=True)
    TOCGameT2L2 = models.IntegerField(null=True)
    xGfPeriodT2L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL3 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L3 = models.IntegerField(null=True)
    possessionGameT1L3 = models.IntegerField(null=True)
    gfPeriodT1L3 = models.IntegerField(null=True)
    gfGameT1L3 = models.IntegerField(null=True)
    gaPeriodT1L3 = models.IntegerField(null=True)
    gaGameT1L3 = models.IntegerField(null=True)
    TOCPeriodT1L3 = models.IntegerField(null=True)
    TOCGameT1L3 = models.IntegerField(null=True)
    xGfPeriodT1L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L3 = models.IntegerField(null=True)
    possessionGameT2L3 = models.IntegerField(null=True)
    gfPeriodT2L3 = models.IntegerField(null=True)
    gfGameT2L3 = models.IntegerField(null=True)
    gaPeriodT2L3 = models.IntegerField(null=True)
    gaGameT2L3 = models.IntegerField(null=True)
    TOCPeriodT2L3 = models.IntegerField(null=True)
    TOCGameT2L3 = models.IntegerField(null=True)
    xGfPeriodT2L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL4 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L4 = models.IntegerField(null=True)
    possessionGameT1L4 = models.IntegerField(null=True)
    gfPeriodT1L4 = models.IntegerField(null=True)
    gfGameT1L4 = models.IntegerField(null=True)
    gaPeriodT1L4 = models.IntegerField(null=True)
    gaGameT1L4 = models.IntegerField(null=True)
    TOCPeriodT1L4 = models.IntegerField(null=True)
    TOCGameT1L4 = models.IntegerField(null=True)
    xGfPeriodT1L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L4 = models.IntegerField(null=True)
    possessionGameT2L4 = models.IntegerField(null=True)
    gfPeriodT2L4 = models.IntegerField(null=True)
    gfGameT2L4 = models.IntegerField(null=True)
    gaPeriodT2L4 = models.IntegerField(null=True)
    gaGameT2L4 = models.IntegerField(null=True)
    TOCPeriodT2L4 = models.IntegerField(null=True)
    TOCGameT2L4 = models.IntegerField(null=True)
    xGfPeriodT2L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L4 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL5 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L5 = models.IntegerField(null=True)
    possessionGameT1L5 = models.IntegerField(null=True)
    gfPeriodT1L5 = models.IntegerField(null=True)
    gfGameT1L5 = models.IntegerField(null=True)
    gaPeriodT1L5 = models.IntegerField(null=True)
    gaGameT1L5 = models.IntegerField(null=True)
    TOCPeriodT1L5 = models.IntegerField(null=True)
    TOCGameT1L5 = models.IntegerField(null=True)
    xGfPeriodT1L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L5 = models.IntegerField(null=True)
    possessionGameT2L5 = models.IntegerField(null=True)
    gfPeriodT2L5 = models.IntegerField(null=True)
    gfGameT2L5 = models.IntegerField(null=True)
    gaPeriodT2L5 = models.IntegerField(null=True)
    gaGameT2L5 = models.IntegerField(null=True)
    TOCPeriodT2L5 = models.IntegerField(null=True)
    TOCGameT2L5 = models.IntegerField(null=True)
    xGfPeriodT2L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L5 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL6 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L6 = models.IntegerField(null=True)
    possessionGameT1L6 = models.IntegerField(null=True)
    gfPeriodT1L6 = models.IntegerField(null=True)
    gfGameT1L6 = models.IntegerField(null=True)
    gaPeriodT1L6 = models.IntegerField(null=True)
    gaGameT1L6 = models.IntegerField(null=True)
    TOCPeriodT1L6 = models.IntegerField(null=True)
    TOCGameT1L6 = models.IntegerField(null=True)
    xGfPeriodT1L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L6 = models.IntegerField(null=True)
    possessionGameT2L6 = models.IntegerField(null=True)
    gfPeriodT2L6 = models.IntegerField(null=True)
    gfGameT2L6 = models.IntegerField(null=True)
    gaPeriodT2L6 = models.IntegerField(null=True)
    gaGameT2L6 = models.IntegerField(null=True)
    TOCPeriodT2L6 = models.IntegerField(null=True)
    TOCGameT2L6 = models.IntegerField(null=True)
    xGfPeriodT2L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    nameL7 = models.CharField(max_length=50, null=True)
    possessionPeriodT1L7 = models.IntegerField(null=True)
    possessionGameT1L7 = models.IntegerField(null=True)
    gfPeriodT1L7 = models.IntegerField(null=True)
    gfGameT1L7 = models.IntegerField(null=True)
    gaPeriodT1L7 = models.IntegerField(null=True)
    gaGameT1L7 = models.IntegerField(null=True)
    TOCPeriodT1L7 = models.IntegerField(null=True)
    TOCGameT1L7 = models.IntegerField(null=True)
    xGfPeriodT1L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT1L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT1L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT1L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    possessionPeriodT2L7 = models.IntegerField(null=True)
    possessionGameT2L7 = models.IntegerField(null=True)
    gfPeriodT2L7 = models.IntegerField(null=True)
    gfGameT2L7 = models.IntegerField(null=True)
    gaPeriodT2L7 = models.IntegerField(null=True)
    gaGameT2L7 = models.IntegerField(null=True)
    TOCPeriodT2L7 = models.IntegerField(null=True)
    TOCGameT2L7 = models.IntegerField(null=True)
    xGfPeriodT2L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGfGameT2L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaPeriodT2L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    xGaGameT2L7 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.nameT1} - {self.nameT2}'
