# Event_Organization

Проект Event_Organization представляет собой систему, которая позволяет пользователям регистрироваться и авторизовываться на портале, создавать какие-либо мероприятия  
и просматривать информацию о них. Так же есть возможность оставлять отзывы и ставить рейтинг для мероприятий <br>
Главные функциональные возможности проекта: <br>
1. Регистрация и авторизация пользователей для доступа к порталу
2. Возможность редактировать профиль и обновлять информацию о себе
3. Создание мероприятий на портале и регистрация на мероприятие
4. Просмотр информации о мероприятиях, владельцы мероприятий могут видеть список участвующих пользователей
5. Отправка уведомления о мероприятии на электронную почту за 1 день до мероприятия
6. Возможность оставлять отзывы с рейтингом о прошедшем мероприятии, владелец мероприятия может удалять отзывы


## Установка

1. Склонируйте репозиторий:
   ```
   git clone git@github.com:AlexaKolacheva/Event_Organization.git
   ```
2. Зайдите в проект
    ```
   cd Event_Organization
    ```
3. Создайте и активируйте виртуальное окружение:
    ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
    ```

4. Убедитесь что у вас установлен redis:
    ```
    ~ % redis-cli
   127.0.0.1:6379> ping
   PONG
   ```
   
5. Соберите Docker-образ и запустите контейнеры:
   Эта команда создаст и запустит Docker-контейнеры для приложения Django, базы данных PostgreSQL, Celery и Redis
    ```
   docker-compose up --build
    ```
  
7. Приложение будет доступно по адресу http://localhost:8000/. <br>


### Настройки доступа
email: alexakola4eva@gmail.com <br>
Password: 123

## Работа с API
 
Документация на swagger:
http://127.0.0.1:8000/swagger/

### Регистрация и авторизация
1. **Регистрация и авторизация**: Для начала работы с сервисом пользователи должны зарегистрироваться и пройти авторизацию <br>
 ***Ссылка для регистрации пользователей:*** http://127.0.0.1:8000/api/auth/users/

2. **Получение токена**: Авторизация пользователей происходит через JWT, и для входа используется email.<br>
 ***Ссылка для получения токена:*** http://127.0.0.1:8000/api/token/


### Создание и управление событиями
1. **Создание события**: Пользователи могут создавать события, включено добавление фотографий, фотографии будут автоматически оптимизированы для уменьшения размера файла.<br>
 ***Ссылка для добавления события:*** http://127.0.0.1:8000/api/auth/events/
2. **Редактирование события**: Только владелец события может редактировать и удалить событие
   ***Ссылка для управления событиями:*** http://127.0.0.1:8000/api/auth/events/{id}/
3. **Регистрация на событие**: Пользователь может выбрать статус, Пойду, Не пойду, Подумаю
   ***Ссылка на регистрацию***: http://127.0.0.1:8000/api/auth/participations/

### Комментарии и отзывы
1. **Создание отзыва**: Пользователи могут оставлять отзывы на прошедшие события и ставить рейтинг, от 1-го до 5-ти. Также, высчитывается средний рейтинг при каждом обновлении
   ***ССылка для отзывов***: http://127.0.0.1:8000/api/activity/reviews/

2.**Редактирование отзывов**: Только владельцы события могут удалять отзыв
  ***ССылка для управления отзывами***: http://127.0.0.1:8000/api/activity/reviews/{id}

**Примечания:**
Убедитесь, что на вашей системе установлены Docker и Docker Compose.<br>
Убедитесь, что Redis запущен на вашем компьютере для выполнения задач Celery.

   

