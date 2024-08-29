from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=200, unique=True
    )  # Название продукта, строка до 200 символов, уникальное
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Цена продукта, десятичное число с 2 знаками после запятой
    description = models.TextField(
        blank=True, null=True
    )  # Описание продукта, текстовое поле, может быть пустым
    quantity = models.PositiveIntegerField(
        default=0
    )  # Количество продукта, положительное целое число, по умолчанию 0

    def __str__(self):
        return self.name
