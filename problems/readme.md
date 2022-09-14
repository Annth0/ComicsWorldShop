--- Leer para no tener problemas en la ejecución de la app --
## desinstalar para tener los mismos que el curso 

virtualenv -p python env
.\env\Scripts\activate

pip install flask==1.1.2
pip install flask-script==2.0.6

/- pip uninstall itsdangerous
/- pip install itsdangerous==1.1.0

/- pip uninstall markupsafe
/- pip install markupsafe==1.1.1

/- pip uninstall werkzeug
/- pip install werkzeug==1.0.1

/- pip install jinja2
/- pip install jinja2==2.11.2


/- python manage.py runserver