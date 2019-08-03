- git clone https://gitlab.com/tutran985/9gag.com.git



- pip install -r  requirements.txt

- instal postgres


cd 9gag.com

edit your settings.py file to connect to the new database.

- python manage.py migrate

- python manage.py createsuperuser

- python manage.py runserver