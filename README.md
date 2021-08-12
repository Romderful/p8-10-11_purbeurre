# Pur Beurre - Openclassrooms project 8

This project offers a plateform for people in need of a snack, but are looking for something healthy.
A quick search can be done from the main page, and the site offers a list of substitutes in the same category, ordered from the best nutriscore to the worst.
If the user created its account and profile, it can also add a product to its favourites.

## Installation

Clone [the repository](https://github.com/Romderful/p8_purbeurre) on your computer.


Set your virtual environment under [python 3.9](https://www.python.org/downloads/release/python-396/)


```bash
pipenv install  # create the virtual environment and install the dependencies
pipenv shell  # activate the virtual environment

touch .env # create a file where you'll put your database configuration and the django secret key

DB_USER="DB_USER"
DB_NAME="DB_NAME"
DB_PASSWORD="DB_PASSWORD"
DB_PORT="DB_PORT"
DJANGO_SECRET_KEY="DJANGO_SECRET_KEY"
```

## Usage

```bash
python manage.py migrate # create the migrations
python manage.py fill_database # use the custom command to implement the dabatase
python manage.py runserver # start the local server
```

## License

[MIT](https://choosealicense.com/licenses/mit/)