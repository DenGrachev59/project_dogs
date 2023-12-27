from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f' {self.name} ({self.description})'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'



class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    # category = models.CharField(max_length=100, verbose_name='Порода')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Порода')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='фото')
    birth_day = models.DateField(**NULLABLE, verbose_name='дата рождения')

    def __str__(self):
        return f' {self.name} ({self.category}) '

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
