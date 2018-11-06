# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# CAMERA
class gallery(models.Model):
	timestamp = models.DateTimeField('date published')
	
class image(models.Model):
	gallery_key = models.ForeignKey(gallery)
	timestamp = models.DateTimeField('date published')
	image = models.ImageField(upload_to = "gallery")

# GPS
class location(models.Model): 
	timestamp = models.DateTimeField('date published')
	latitude = models.IntegerField(default=0)
	longitude = models.IntegerField(default=0)
	altitude = models.IntegerField(default=0)
	
	def __str__(self):
		return '[timestamp: {}, latitude: {}, longitude: {}, altitude: {}]'.format(self.timestamp, self.latitude, self.longitude, self.altitude)

# ACCELOROMETER
class acceleration(models.Model):
	timestamp = models.DateTimeField('date published')
	x_accel = models.IntegerField(default=0)	
	y_accel = models.IntegerField(default=0)
	z_accel = models.IntegerField(default=0)
	x = models.IntegerField(default=0)	
	y = models.IntegerField(default=0)
	z = models.IntegerField(default=0)
	
	def __str__(self):
		return '[timestamp: {}, x_accel: {}, y_accel: {}, z_accel: {}, x: {}, y: {}, z: {}]'.format(self.timestamp, self.x_accel, self.y_accel, self.z_accel, self.x, self.y, self.z)
		
# TEMPERATURE
class temperature(models.Model):
	timestamp = models.DateTimeField('date published')
	temperature = models.IntegerField(default=0)
	
	def __str__(self):
		return '[timestamp: {}, temperature: {}]'.format(self.timestamp, self.temperature)
		
		
# HUMIDITY
class humidity(models.Model):
	timestamp = models.DateTimeField('date published')
	humidity = models.IntegerField(default=0)
	
	def __str__(self):
		return '[timestamp: {}, humidity: {}]'.format(self.timestamp, self.humidity)