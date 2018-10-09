import csv
from datetime import time
from eatatdcu.models import Campus, Restaurant
    
with open('../../data/campus.csv') as ca:
   reader = csv.reader(ca)
   for row in reader:
      campus = Campus(int(row[0]),row[1])
      campus.save()

with open('../../data/restaurant.csv') as re:
   reader = csv.reader(re)
   for row in reader:
       opening = row[4].split(':')
       closing = row[5].split(':')
       restaurant = Restaurant(int(row[0]),row[1],row[2],int(row[3]),
               time(hour=int(opening[0]),minute=int(opening[1])),
               time(hour=int(closing[0]),minute=int(closing[1])),
               int(row[6]),int(row[7]))
       restaurant.save()
