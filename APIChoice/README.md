# Опрос пользователей (Django REST Framework)
__*Задача: спроектировать и разработать API для системы опросов пользователей.*__

*Функционал для администратора системы:*

- *авторизация в системе (регистрация не нужна)*
- *добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя*
- *добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)*

*Функционал для пользователей системы:*

- *получение списка активных опросов*
- *прохождение опроса: в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов*
- *получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя*

Использовать следующие технологии: Django 2.2.10, Django REST framework.

## Как использовать

- Создайте виртуальное окружение: ```virtualenv -p python3 env```
- Активируйте виртуальное окружение: ```source env/bin/activate```
- Установите зависимости: ```pip install -r requirements.txt```
- Создайте миграции: ```python manage.py migrate```
- Загрузите БД: ```python manage.py loaddata db.json```
- Запустите сервер: ```python manage.py runserver```
- Откройте API документацию: http://127.0.0.1:8000/api/swagger

## Запуск при помощи докера

- ```docker-compose build```
- ```docker-compose up```
- Откройте API документацию: http://127.0.0.1:8000/api/swagger


## Информация для входа

В системе есть 1 роль - администратор.  
Авторизация при переходе на url: http://127.0.0.1:8000/api/admin/  
*username* : ```admin```  
*password* : ```admin```  
