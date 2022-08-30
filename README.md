## create virtual environment
````
python -m venv env
````

## install dependencies
````
pip install -r requirements.txt
````

## activate virtual environment
in the window
````
env\scripts\active.bat
````

## como roda o projeto
````
set FLASK_ENV=development
set FLASK_APP=app.py
flask run
````