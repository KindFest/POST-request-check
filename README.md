# Web-приложение для определения заполненных форм.

Приложение позволят получить данные из POST запроса, сделать валидацию полей на предмет их значений (email, phone, date, text) и проверить с шаблонами из базы данных.
Результат проверки:
- имя шаблона, которому соответствуют введенные данные
либо
- названия полей, которым нет соответствия в базе банных

Состав приложения:
main.py - веб-приложение
test_script.py - скрипт для проверки работоспособности приложения. Запускать после запуска веб-приложения
templates_db.py - скрипт для наполнения базы данных новыми шаблонами.
type_validation.py - модуль, в котором реализована валидация введенных значений


## Стек

- Python (3.10)
- TinyDB (4.7.0)
- requests (2.28.1)


## Лицензия

X11
