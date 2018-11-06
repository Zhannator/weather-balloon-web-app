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