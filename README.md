# zerometro
[under construction]

How many games can someone finish?

## Dependencies
- Python 3.11+
- PostgreSQL 13+

## Run application
First, create a database on postgres called "zerometro".

Then, install all requirements listed on `requirements.txt` and run:
`python manage.py migrate && python manage.py runserver`.

Note: For now, only admin panel is available. Access localy by `http://localhost:8000/admin/`.

## Tests
Install all requirements listed on `requirements.dev.txt` and run `python manage.py test`.

## Code lint
Install black (`pip install black`) and run `black .`

## Create an admin superuser
Run `python manage.py createsuperuser`.
