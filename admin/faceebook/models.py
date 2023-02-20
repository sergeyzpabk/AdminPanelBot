from django.db import models

# Create your models here.

class Urls(models.Model):
    url = models.CharField('Ссылка', max_length=250)
    def __str__(self):
        return f'{self.url}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
