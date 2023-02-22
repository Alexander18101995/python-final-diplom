from django.db import models
from rest_framework.authtoken.admin import User


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь',
                                blank=True, null=True,
                                on_delete=models.CASCADE)
    state = models.BooleanField(verbose_name='статус получения заказов', default=True)


    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Список магазинов"
        ordering = ('-name',)





