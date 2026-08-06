# Group Portal / Портал Групи

[English](#english) | [Українська](#українська)

---

<a name="english"></a>
## 🇬🇧 English

A modern web portal for team collaboration, studying, and event organization. Built with **Django** and **Django REST Framework**.

### Features
- **Authentication:** Local registration/login and Google OAuth 2.0 integration.
- **Communication:** Discussion forum and announcements system.
- **API Documentation:** Auto-generated OpenAPI 3.0 documentation via `drf-spectacular` (Swagger UI & ReDoc).
- **Security:** Secure POST-based logout with CSRF protection and allowed hosts validation.
- **Moderation:** Dedicated moderation panel for staff and administrators.

### Installation & Setup

#### 1. Prerequisites
- Python 3.10+
- `pip`

#### 2. Installation
```bash
# Clone the repository
git clone <repository_url>
cd group-portal

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Configuration
Create a `.env` file in the root directory and configure environment variables:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

#### 4. Running the Project
```bash
# Run database migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

#### 5. API Documentation
Once the server is running, access the interactive API docs at:
`http://127.0.0.1:8000/api/schema/swagger-ui/`

---

<a name="українська"></a>
## 🇺🇦 Українська

Сучасний веб-портал для командної роботи, навчання та організації подій. Розроблений на базі **Django** та **Django REST Framework**.

### Можливості
- **Авторизація:** Локальна реєстрація/вхід та інтеграція з Google OAuth 2.0.
- **Комунікація:** Форум для обговорень та система оголошень.
- **API Документація:** Автоматично згенерована документація OpenAPI 3.0 за допомогою `drf-spectacular` (Swagger UI та ReDoc).
- **Безпека:** Безпечний вихід із системи через POST-запит із CSRF-захистом та валідацією хостів.
- **Модерація:** Спеціальна панель модерації для персоналу та адміністраторів.

### Встановлення та запуск

#### 1. Передумови
- Python 3.10+
- `pip`

#### 2. Встановлення
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

#### 3. Налаштування
Створіть файл `.env` у кореневій папці проєкту та додайте змінні середовища:
```env
SECRET_KEY=ваш_секретний_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GOOGLE_CLIENT_ID=ваш_id_google
GOOGLE_CLIENT_SECRET=ваш_секрет_google
```

#### 4. Запуск проєкту
```bash
# Виконання міграцій бази даних
python manage.py migrate

# Створення суперкористувача
python manage.py createsuperuser

# Запуск сервера розробки
python manage.py runserver
```

### 5. API Документація
Після запуску сервера інтерактивну документацію можна знайти за адресою:
`http://127.0.0.1:8000/api/schema/swagger-ui/`
