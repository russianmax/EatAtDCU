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