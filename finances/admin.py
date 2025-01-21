from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_type",
        "amount",
        "category",
        "date",
    )  # Поля для отображения
    list_filter = ("transaction_type", "category")  # Фильтрация
    search_fields = ("category", "description")  # Поиск по категориям и описаниям
