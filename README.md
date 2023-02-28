После клонирования проекта для запуска используйте следующие команды:\n
'docker compose build'\n
'docker compose up'


После выполнения этих команд зайдите в Docker контейнер по команде:
'docker exec -it <Your conteiner id> bash'


После входа в контейнер пропишите следующие команды:
'python manage.py makemigrations'
'python manage.py migrate'
'python manage.py first_csv --path markets/scripts/location.csv' Для заполнения городов
'python manage.py second_csv --path markets/scripts/product.csv' Для заполнения продуктов

Для входа в админку создать юзера по команде:
'python manage.py cratesuperuser'



