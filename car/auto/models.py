from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=20,verbose_name="название")
    speed = models.FloatField(verbose_name="скорость")
    costs = models.IntegerField(verbose_name="стоимость")
    description = models.TextField(verbose_name="описание")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        # ordering = ['id', 'title']
