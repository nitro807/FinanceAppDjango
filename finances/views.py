from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, TransactionForm, CategoryForm
from .models import Transaction, Category
from django.db.models import Sum


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # После успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def transactions(request):
    user_transactions = Transaction.objects.filter(user=request.user)

    # Сумма доходов и расходов
    income_total = (
        user_transactions.filter(transaction_type="income").aggregate(Sum("amount"))[
            "amount__sum"
        ]
        or 0
    )
    expense_total = (
        user_transactions.filter(transaction_type="expense").aggregate(Sum("amount"))[
            "amount__sum"
        ]
        or 0
    )

    return render(
        request,
        "finances/transactions.html",
        {
            "transactions": user_transactions,
            "income_total": income_total,
            "expense_total": expense_total,
        },
    )


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = (
                request.user
            )  # Привязываем транзакцию к текущему пользователю
            transaction.save()
            return redirect(
                "transactions"
            )  # После добавления — редирект на список транзакций
    else:
        form = TransactionForm()
    return render(request, "finances/add_transaction.html", {"form": form})


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "finances/transactions.html", {"transactions": transactions})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user  # Привязываем категорию к пользователю
            category.save()
            return redirect("category_list")  # Редирект на список категорий
    else:
        form = CategoryForm()
    return render(request, "finances/add_category.html", {"form": form})


def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, "finances/category_list.html", {"categories": categories})


def home(request):
    return render(request, "finances/home.html")
