# Pur Beurre - Openclassrooms project 8-11

This project offers a platform for people in need of a product's substitute having an equal or a better nutriscore grade.
A quick search can be done from the main page, also from the navbar, it will return a list of substitutes corresponding to the searched product's categories.
If the user created his account, he will also be able to add a product to his favourites.

The project can be seen at this address : https://rr-purbeurre.herokuapp.com/

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

create a database using postgresql having the same name as DB_USER

python manage.py migrate # create the migrations
python manage.py fill_database # use the custom command to implement the dabatase
python manage.py runserver # start the local server
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
