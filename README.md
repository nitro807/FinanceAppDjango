# FinanceAppDjango  

## Описание  
FinanceAppDjango — это приложение для управления личными финансами. Оно позволяет пользователям добавлять категории, записывать транзакции и анализировать свои расходы.  

## Установка  

### 1. Клонирование репозитория  
```bash
git clone https://github.com/USERNAME/FinanceAppDjango.git
cd FinanceAppDjango

### 2. Настройка виртуального окружения
python -m venv venv
source venv/Scripts/activate  # Для Windows
# или
source venv/bin/activate  # Для Linux/Mac

### 3. Установка зависимостей
pip install -r requirements.txt

### 4. Настройка .env файла
Создайте файл .env в корневой директории и укажите:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/your_database_name
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password

### 5. Применение миграций
python manage.py migrate

### 6. Запуск сервера
python manage.py runserver

## Лицензия
MIT License
