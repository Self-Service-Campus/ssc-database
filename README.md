# database

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2b76aa6a97d747f9b39c3aa32d6316a7)](https://app.codacy.com/gh/Self-Service-Campus/ssc-database?utm_source=github.com&utm_medium=referral&utm_content=Self-Service-Campus/ssc-database&utm_campaign=Badge_Grade_Settings)

./manage.py graph_models -a --hide-edge-labels -o db_model.png

## How to install

Make sure you are running Python 3.5.

`$ virtualenv -p python3 venv`

## How to run

`$ source ./venv/bin/activate`

## How to clean the database

`find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`

`find . -path "*/migrations/*.pyc"  -delete`

DELETE DB.SQLITE3

`python3 manage.py makemigrations`

`python3 manage.py makemigrations ssc_db_api_APP`

`python3 manage.py migrate`

`python3 manage.py runserver`

## How to load the database

www.localhost:8080/load_db/
