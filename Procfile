release: python manage.py makemigrations && python manage.py migrate
web: gunicorn adv_project.wsgi:application --log-file - 