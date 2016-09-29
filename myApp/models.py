# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class myModel(models.Model):
    class Meta:
        verbose_name = "Meu Modelo"

    atributo_string = models.CharField(max_length=50)
    atributo_int = models.IntegerField(default=0)
    atributo_boolean = models.BooleanField(default=False)

    def __unicode__(self):
        return self.atributo_string

    def getAtributo_string(self):
        return self.atributo_string

    def setAtributo_string(self, valor):
        self.atributo_string = valor
        self.save()

    @staticmethod
    def divisaoValores(valor1, valor2):
        try:
            total=valor1/valor2
            return total
        except Exception as e:
            raise ValidationError(u"Não é possivel dividir esses numeros")

# SIGNALS
from django.db.models import signals
def myModel_post_save(signal, instance, sender, created, **kwargs):    
    if created:
        instance.atributo_boolean = True
signals.post_save.connect(myModel_post_save, sender=myModel)
        