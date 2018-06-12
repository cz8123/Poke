from django.db import models
from poke.models import Pokemon, Move, Item, Type, Ability
# class Iteminfo310(models.Model):
#     name = models.CharField(max_length=20)
#     ranking = models.IntegerField()
#     usageRate = models.FloatField()
#     sequenceNumber = models.IntegerField()
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
# class Wazainfo310(models.Model):
#     name = models.CharField(max_length=20)
#     typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
#     usageRate = models.FloatField()
#     sequenceNumber = models.IntegerField()
#     move = models.ForeignKey(Move, on_delete=models.CASCADE)
# class Seikakuinfo310(models.Model):
#     name = models.CharField(max_length=10)
#     ranking = models.IntegerField()
#     usageRate = models.FloatField()
#     sequenceNumber = models.IntegerField()
#     detail = models.TextField()
# class Tokuseiinfo310(models.Model):
#     name = models.CharField(max_length=10)
#     ranking = models.IntegerField()
#     usageRate = models.FloatField()
#     sequenceNumber = models.IntegerField()
#     ability = models.ForeignKey(Ability, on_delete=models.CASCADE)

# class Pglpokemon310(models.Model):
#     name = models.CharField(max_length=10)
#     formNo = models.CharField(max_length=5)
#     monsno = models.IntegerField()
#     ranking = models.IntegerField()
#     typeId1 = models.ForeignKey(Type, on_delete=models.CASCADE)
#     typeId2 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='typeid2', blank=True, null=True)
#     formName = models.CharField(max_length=10, blank=True)
#     pokemonId = models.CharField(max_length=15)
#     sequenceNumber = models.IntegerField()
#     iteminfo = models.ManyToManyField(Iteminfo, blank=True, null=True)
#     wazainfo = models.ManyToManyField(Wazainfo, blank=True, null=True)
#     seikakuinfo = models.ManyToManyField(Seikakuinfo, blank=True, null=True)
#     tokuseiinfo = models.ManyToManyField(Tokuseiinfo, blank=True, null=True)
