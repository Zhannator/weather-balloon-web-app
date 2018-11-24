# username: balloon-master
# password: iamyourmaster

# Public libraries
import django
from django.utils import timezone

# Private libraries
from data.models import gallery, image, location, acceleration, temperature, humidity

# Database commands examples
gps.objects.all()
l = location(timestamp = timezone.now(), latitude = 0, longitude = 1, altitude = 2)
l.save()
location.objects.all()
l = location.objects.get(id = 1)
location.objects.filter(latitude = 0)


# Update models
python manage.py makemigrations data
python manage.py sqlmigrate data 0001
python manage.py migrate

# Run server
python manage.py runserver

# Run shell
python manage.py shell

# Upload image
from data.models import image, location, acceleration, temperature, humidity
from django.utils import timezone
from django.core.files import File
reopen = open(“2018-11-1108.jpg”, “rb”)
django_file = File(reopen)
i = image()
i.timestamp = timezone.now()
i.image.save(“data/test.jpg”, django_file, save = True)
i.save()

##### EXAMPLE DATABASE INTEGRATION ######
import os
import sqlite3
import datetime
from django.core.files import File

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):  
    con = sqlite3.connect(db_path)
    return con

def create_temperature(con, now, temperature):  
	cur = con.cursor() # instantiate a cursor obj
	product_sql = '''
				INSERT INTO data_temperature (timestamp, temperature)
				VALUES (?, ?)'''
	cur.execute(product_sql, (now, temperature))
	return cur.lastrowid # Return unique id of the just added item

def insert_image(con, now, image_filename):
	cur = con.cursor() # instantiate a cursor obj
	sql = '''
		INSERT INTO data_image (timestamp, image, gallery_key_id)
		VALUES(?, ?, ?);'''
	cur.execute(sql,(now, "gallery/" + image_filename, 1))
	return cur.lastrowid # Return unique id of the just added item
	
# Connect to the database
con = db_connect()
# Make changes
temperature = 10
try:
	create_temperature(con, datetime.datetime.now(), temperature)
	# Commit changes to database
	con.commit()
except:
	# rollback all database actions since last commit
    con.rollback()
    raise RuntimeError("Database update error occured...")
	
con.close()
##### EXAMPLE DATABASE INTEGRATION ######