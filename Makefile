run-server: migrate
	python manage.py runserver

test:
	python -Wa manage.py test

black:
	black .

django-shell:
	python manage.py shell

make-migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate
