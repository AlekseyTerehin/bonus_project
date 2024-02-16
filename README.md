# Тестовое задание

На backend части реализованы эндпоинты:
1. Авторизация по JWT-токену
2. Регистрация
3. Получение списка пользователей с бонусной программой
4. Предоставление случайного бонуса пользователю.
5. Подключен swagger по url http://127.0.0.1:8000/api/schema/swagger-ui/

Запуск проекта:
1. Скачать репозиторий
2. В корневой директории создать файл .env с переменными окружения по образцу .env_example из репозитория
3. Создать образы докера docker-compose build
4. Запустить приложение docker-compose up -d
5. Загрузить фикстуры с тестовыми данными включая администратора - логин: admin пароль:admin - docker exec django python3 /usr/src/app/backend/manage.py  loaddata /usr/src/app/backend/db.json
6. Выполнить запуск тестов - docker exec django python3 /usr/src/app/backend/manage.py test /usr/src/app/backend/

Посмотреть коэффициент покрытия кода тестами:
- в консоле: docker exec django coverage report
- в браузере: docker exec django coverage html (в корневой папке создатся директория htmlcov в которой будет расположен index.html)

