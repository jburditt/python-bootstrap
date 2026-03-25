# PYTHON BOOTSTRAP DJANGO
A Python Bootstrap project using Django

## REQUIREMENTS
- Python 3

## WINDOWS INSTALLATION
- Run `py -3 -m venv .venv` to create virtual environment
- Run `.venv/Scripts/activate` to activate the environment
- Optionally run `python.exe -m pip install --upgrade pip` to upgrade PIP
- Run `pip install Django` to install Django
- Run `pip install django-debug-toolbar` to install the debug toolbar
- Run `pip install django-cors-headers` to install Django CORS headers
- Add PATH 'C:\Users\<user>\AppData\Local\Python\pythoncore-3.14-64\Scripts' for 'django-admin' command

## RUNNING
- Change folder to 'api'
- Run `py manage.py runserver 8080`

## UNIT TESTS
- Run `py manage.py test polls`

## HOW-TO
- Create project `django-admin startproject bootstrap api`
- Add app `py manage.py startapp polls`
- Add database migration `py manage.py makemigrations`
- Run database migrations `py manage.py migrate`
