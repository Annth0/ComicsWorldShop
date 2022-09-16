--- Leer para no tener problemas en la ejecución de la app --
### desinstalar para tener los mismos que el curso 

## módulos 1 y 2

virtualenv -p python env
.\env\Scripts\activate

/- python manage.py runserver


pip install flask==1.1.2
pip install flask-script==2.0.6

/- pip uninstall jinja2
/- pip install jinja2==2.11.2

/- pip uninstall itsdangerous
/- pip install itsdangerous==1.1.0

/- pip uninstall markupsafe
/- pip install markupsafe==1.1.1

/- pip uninstall werkzeug
/- pip install werkzeug==1.0.1

## para modulo 3

/- pip install flask-WtF==0.14.3
/- pip install WTForms==2.3.3

/- python manage.py runserver

## para modulo 4

/- pip install  flask-mysql==1.5.2  
/- pip install  flask-mysqldb==0.2.0
-----   pip3 install mysql

- pip3 uninstall mysqlclient
pip3 install mysqlclient==2.0.3 - si no funciona: 
pip3 install mysql 

## para modulo 5

### 5.3
/- pip install flask-login==0.5.0

-- from flask_login import LoginManager, login_user

-- from flask_login import UserMixin
