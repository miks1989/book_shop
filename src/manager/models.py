from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'кніга'
        verbose_name_plural = 'кнігі'

    title = models.CharField(max_length=100, verbose_name='назва кнігі')
