from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Sdelka(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return f'{self.name}'    

    class Meta:
        pass

class CounterAgent(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.name}'

class CellValue(MPTTModel):
    sdelka = models.ForeignKey(Sdelka, on_delete=models.CASCADE)
    counteragent = models.ForeignKey(CounterAgent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.name}'
    

    class MPTTMeta:
        order_insertion_by = ['name']

class PredmetOcenki(models.Model):
    name = models.CharField(max_length=1000)
    sdelka = models.ForeignKey('change_csv.Sdelka', on_delete=models.DO_NOTHING)
    counteragent = models.ForeignKey('change_csv.CounterAgent', on_delete=models.DO_NOTHING)
