from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("transactions/", views.transactions, name="transactions"),  # Список транзакций
    path(
        "add/", views.add_transaction, name="add_transaction"
    ),  # Добавление транзакции
    path("add_category/", views.add_category, name="add_category"),
    path("categories/", views.category_list, name="category_list"),
    path("", views.home, name="home"),  # Главная страница
]
