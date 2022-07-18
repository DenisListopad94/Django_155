from django.db import models

class CommenModel(models.Model):
    topic = models.CharField(max_length=20,verbose_name="тема")
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.topic

class Car(models.Model):
    title = models.CharField(max_length=20, verbose_name="название")
    speed = models.FloatField(verbose_name="скорость")
    costs = models.IntegerField(verbose_name="стоимость")
    description = models.TextField(verbose_name="описание")
    man = models.ForeignKey("Manufacture", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        # ordering = ['id', 'title']


class Manufacture(models.Model):
    country = models.CharField(max_length=30, verbose_name="страна")
    city = models.CharField(max_length=20, verbose_name="город")
    worker = models.IntegerField(verbose_name="количество работников")
    director = models.OneToOneField("Director", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'


class Provider(models.Model):
    name = models.CharField(max_length=30, verbose_name="поставщик")
    finance = models.IntegerField(verbose_name="годовой доход")
    detail = models.TextField(verbose_name="детали")
    manprov = models.ManyToManyField("Manufacture")
    car = models.ForeignKey("Car", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщик'


class Director(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя")
    surname = models.CharField(max_length=20, verbose_name="фамилия")
    age = models.IntegerField(verbose_name="возраст")
    email = models.TextField(verbose_name="контактные данные")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директор'
