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
ALLOWED_HOSTS = ['127.0.0.1', 'username.pythonanywhere.com']
```
3. Create a zip of src and data directories which are found in **2019-ca377-maksimk2-EatAtDCU**
4.Upload zip to the pythonanwhere via upload button
5.Extract your files in the console
```
tar zxvf src.tar.gz
tar zxvf data.tar.gz
```
