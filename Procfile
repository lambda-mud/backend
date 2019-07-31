release: python manage.py migrate && python util/create_world.py
web: gunicorn adv_project.wsgi:application --log-file - 