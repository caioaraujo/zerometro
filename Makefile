run-server: migrate
	python manage.py runserver

black:
	black .

django-shell:
	python manage.py shell

make-migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test: migrate
	python -Wa manage.py test
