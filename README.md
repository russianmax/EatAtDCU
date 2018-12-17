# EAT at DCU

This app allows users to look for places to eat on any of the DCU campuses. The campuses are as follows: 
1. Glasnevin
2. St Pats
3. All Hallows
4. DCU Alpha

## Instalation 
To run locally, install

1. Python 3.x and up
2. Django 1.11 version
3. Request and pip
4. Git ( if you want clone through the console)

Now, clone my repository, it can be found at: https://gitlab.computing.dcu.ie/maksimk2/2019-ca377-EatAtDCU.git
In the terminal, do the following:
```
cd < where you want to clone the project > 
git clone https://gitlab.computing.dcu.ie/maksimk2/2019-ca377-EatAtDCU.git*
cd 2019-ca377-maksimk2-EatAtDCU/src/ca377 
python3/python manage.py makemigrations 
python3/python manage.py migrate 
python3/python manage.py runserver 
```
Head over to your browser, and type in http://127.0.0.1:8000/

## Deploying on pythonanywhere.com
1. Login with your credentials into pythonanywhere.com
2. Edit ca377/settings.py and add pythonanwhere to the list of ALLOWED HOSTS
```
ALLOWED_HOSTS = ['127.0.0.1', 'yourusername.pythonanywhere.com']
```
3. Create a zip of src and data directories which are found in 2019-ca377-maksimk2-EatAtDCU
4.Upload zip to the pythonanwhere via upload button
5.Extract your files in the console
```
tar zxvf src.tar.gz
tar zxvf data.tar.gz
```
6. Make Django virtualenv
```
--python=/usr/bin/python3.5 eatatdcu-virtualenv
```
7. Instal requests and pip
```
pip install django==1.11
pip install requests
```
8. Create a new web app by clicking *Add a new web app*
9. Choose 3.5 as a Django version
10. Edit the working code directory and set it to
```
path = '/home/yourusername/src/ca377'
```
11. Add your virtualenv
```
/home/yourusername/.virtualenv/eatatdcu-virtualenv
```
12. Edit WSGI file, it needs to look like this
```
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/maksimk2/mysite/mysite/settings.py'
## and your manage.py is is at '/home/maksimk2/mysite/manage.py'
path = '/home/maksimk2/src/ca377'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ca377.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
13. Go back to the console and set up your database
```
./manage.py makemigrations
" " 		migrate
" "			shell
import load_db_data
```
14. Check if it works: www.yourusername.pythonanwhere.come