# Тестовое задание

На backend части реализованы эндпоинты:
1. Авторизация по JWT-токену
2. Регистрация
3. Получение списка пользователей с бонусной программой
4. Предоставление случайного бонуса пользователю.
5. Подключен swagger по url api/schema/swagger-ui/

Запуск проекта:
1. Скачать репозиторий
2. В корневой директории создать файл .env с переменными окружения по образцу .env_pattern из репозитория
3. Создать образы докера docker-compose build
4. Запустить приложение docker-compose up -d
5. Загрузить фикстуры с тестовыми данными включая администратора - логин: admin пароль:admin - docker exec <имя_контейнера_django> python3 /usr/src/app/backend/manage.py  loaddata /usr/src/app/backend/db.json
6. Выполнить запуск тестов - docker exec <имя_контейнера_django> python3 /usr/src/app/backend/manage.py test .
