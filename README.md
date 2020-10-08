# Zoo API
## Стек
Python, Django, DjangoRestFramework, Django-Filter
## Функциональные возможности
API содержит четыре модели.

Животное (Animal). Поля: name, description, created_at, updated_at, animal_place, animal_type, employee, employee_assign_date

Вид животного (AnimalType). Поля: name, description, created_at, updated_at, preferable_food, additional_information

Место животного в зоопарке (AnimalPlace). Поля: name, description, created_at, updated_at, specifications, additional_information

Сотрудник (Employee). Поля: first_name, last_name, created_at, updated_at, possition, qualification

## Запуск проекта
На локальном компьютере должен быть установлен Python 3 или выше.

1. Склонировать данный репозиторий на свой локальный компьютер.
2. Установить виртуальное окружение используя команду `python3 -m venv venv`.
3. Установить необходимые библиотеки используя команду `pip install -r requirements.txt`.
4. Выполнить миграции командой `python manage.py migrate`.
5. Запустить локальный сервер командой `python manage.py runserver`.

## Доступные методы API
Endpoint | Методы | Описание
------------ | ------------- | -------------
api/animals/ | GET, POST | Получение списка/создание животных
api/animals/{int:id}/ | GET, PUT, PATCH, DELETE | Получение конкретного животного, его изменение, удаление
api/types/ | GET, POST | Получение списка/создание видов животных
api/types/{int:id}/ | GET, PUT, PATCH, DELETE | Получение конкретного вида животного, его изменение, удаление
api/places/ | GET, POST | Получение списка/создание мест для животных
api/places/{int:id}/ | GET, PUT, PATCH, DELETE | Получение конкретного места животного, его изменение, удаление
api/employees/ | GET, POST | Получение списка/создание работников
api/employees/{int:id}/ | GET, PUT, PATCH, DELETE | Получение конкретного работника, его изменение, удаление

## Фильтрация и сортировка
При получении списка объектов модели его можно фильтровать и сортировать по всем имеющимся полям модели. 

Для этого в params GET запроса нужно передать:

- для фильтрации: `<название фильтруемого поля модели>=<значение>`.
- для сортировки: `ordering=<название поля по которому сортируем>`. Перед названием поля можно добавить `-` для сортировки в обратном порядке.

Также для некоторых моделей есть дополнительные виды фильтрации:

Animal (api/animals/):

- `one_year_employee=true/false`. `true` для того, чтобы выбрать животных, за которыми закреплен один и тот же сотрудник
более 1 года. `false` - наоборот.
- `place_spec=<значение>`. Выбрать животных по характеристикам места в зоопарке.

AnimalPlace (api/places/):

- `two_animals=true/false`. `true` для того, чтобы выбрать место, где содержатся минимум два вида животных. `false` - наоборот.
