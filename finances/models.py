from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    INCOME = "income"
    EXPENSE = "expense"

    TRANSACTION_TYPES = [
        (INCOME, "Доход"),
        (EXPENSE, "Расход"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма транзакции
    transaction_type = models.CharField(
        max_length=7, choices=TRANSACTION_TYPES, default=EXPENSE
    )  # Тип транзакции (доход или расход)
    category = models.ForeignKey(
        "finances.Category", on_delete=models.CASCADE, null=False
    )
    description = models.TextField(blank=True)  # Описание транзакции
    date = models.DateTimeField(auto_now_add=True)  # Дата создания транзакции

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount} ({self.category})"
