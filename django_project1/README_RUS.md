# Система управления продуктами на Django
Простая система управления продуктами, разработанная с использованием Django. Позволяет добавлять продукты с деталями, такими как название, цена, описание и количество.

## Использование
После настройки проекта вы можете добавить продукт, перейдя по адресу `/products/create`. Здесь вы можете ввести название, цену, описание и количество продукта. После заполнения формы нажмите кнопку отправки, чтобы сохранить продукт в базе данных.

# Технические детали
Проект использует Django ORM для взаимодействия с базой данных. Модель `Product` содержит поля для `name`, `price`, `description` и `quantity`. Для обработки запросов используется Django REST Framework.
