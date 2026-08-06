# Портал Групи (Group Portal)

Це сучасний веб-портал для командної роботи, навчання та організації подій. Проєкт побудований на базі **Django** та **Django REST Framework**.

## Функціонал
- **Авторизація:** Локальна реєстрація/вхід та інтеграція з Google OAuth 2.0.
- **Комунікація:** Форум для обговорень та система оголошень.
- **API:** Автоматично згенерована документація (Swagger UI та ReDoc) на базі `drf-spectacular`.
- **Безпека:** Захищений вихід із системи (POST-запит), перевірка хостів для редіректів.
- **Модерація:** Спеціальна панель для модераторів та адміністраторів.

## Інструкція зі встановлення

### 1. Передумови
- Python 3.10+
- `pip`

### 2. Встановлення
```bash
# Клонування репозиторію
git clone <repository_url>
cd group-portal

# Створення та активація віртуального середовища
python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для Linux/macOS:
source .venv/bin/activate

# Встановлення залежностей
pip install -r requirements.txt
```

### 3. Налаштування
Створіть файл `.env` у кореневій папці проєкту та додайте необхідні змінні:
```env
SECRET_KEY=ваш_секретний_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GOOGLE_CLIENT_ID=ваш_id_google
GOOGLE_CLIENT_SECRET=ваш_секретний_ключ_google
```

### 4. Запуск
```bash
# Міграції бази даних
python manage.py migrate

# Створення суперкористувача
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

### 5. Доступ до API
Після запуску документацію можна знайти за адресою:
`http://127.0.0.1:8000/api/schema/swagger-ui/`
