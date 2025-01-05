# zerometro
[under construction]

A simple game tracker.

Track all games that you have already finished, completed (with all trophies, achievments etc) or 
to add into your wish list to play.

## Dependencies
- Python 3.13+
- PostgreSQL 13+

## Setup
Is highly recommended to create a [virtualenvironment](https://docs.python.org/3/library/venv.html).

After create and [activate](https://docs.python.org/3/library/venv.html#how-venvs-work) the virtual environment,
install all dependencies. Using pip: `pip install -r requirements.dev.txt`.

## Run application
First, create a database on postgres called "zerometro".

Then, install all requirements listed on `requirements.txt` and run:
`python manage.py migrate && python manage.py runserver`.

## Tests
Install all requirements listed on `requirements.dev.txt` and run `python manage.py test`.

## Code lint
Install black (`pip install black`) and run `black .`

## Create an admin superuser
Run `python manage.py createsuperuser`.

## URLs
- `/admin`: Django's admin panel. Requires a superuser role to access;
- `/`: Redirect to `/games`;
- `/games`: Load all games catalog;
- `/game/{game_id}`: Fetch a game with form to track the game. Login is required;
- `/cadastro`: User register form;
- `/login`: Self explained;
- `/logout`: Self explained.
