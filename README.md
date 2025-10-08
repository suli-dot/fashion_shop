Перейти в папку проекта
cd C:\programing\fashion_shop
Активировать виртуальное окружение
venv\Scripts\activate
Запустить сервер
python manage.py runserver
Миграции (если менялись модели)
python manage.py makemigrations
python manage.py migrate
Создать суперпользователя
python manage.py createsuperuser
Проверить версию Django
python -m django --version
Настройки Email (уведомления)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"  # пароль приложения
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = "your_admin_email@gmail.com"
