# -*- coding: utf-8 -*-

# Public Libraries
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from collections import OrderedDict
from fusioncharts import FusionCharts
import datetime
import json

# Local libraries
from .models import gallery, image, location, acceleration, temperature, humidity

# Create your views here.
# Data Page
def graph_data(request):
	# --------------------------- TEMPERATURE ---------------------------

	#Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
	dataSource_1 = OrderedDict()

	# The `chartConfig` dict contains key-value pairs of data for chart attribute
	chartConfig_1 = OrderedDict()
	chartConfig_1["caption"] = "Temperature"
	chartConfig_1["yAxisName"] = "Temperature (Celcius)"
	chartConfig_1["xAxisName"] = "Time (seconds since launch)"
	#chartConfig_1["xaxismaxvalue"] = "60"
	#chartConfig_1["xaxisminvalue"] = "0"
	#chartConfig_1["yaxismaxvalue"] = "100"
	chartConfig_1["theme"] = "ocean"

	dataSource_1["chart"] = chartConfig_1
	dataSource_1["dataset"] = []
	
	datasetConfig_1 = OrderedDict()
	datasetConfig_1["drawline"] = "1"
	#datasetConfig_1["seriesname"] = "Server 1"
	#datasetConfig_1["color"] = "#127fcb"
	datasetConfig_1["anchorsides"] = "3"
	datasetConfig_1["anchorradius"] = "8"
	#datasetConfig_1["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_1["anchorbordercolor"] = "#127fcb"
	datasetConfig_1["data"] = []
	
	#Iterate through the most recent 10 entries
	x = 0
	for key in temperature.objects.order_by('timestamp'):
		data = {}
		data["x"] = x
		data["y"] = key.temperature
		datasetConfig_1["data"].append(data)
		x = x + 10

	dataSource_1["dataset"].append(datasetConfig_1)
		
	# Create an object for the column 2D chart using the FusionCharts class constructor
	# The chart data is passed to the `dataSource` parameter.
	temperatureChart = FusionCharts("selectscatter", "ex1", "700", "400", "chart-1", "json", json.dumps(dataSource_1))

	# --------------------------- HUMIDITY ---------------------------

	#Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
	dataSource_2 = OrderedDict()

	# The `chartConfig` dict contains key-value pairs of data for chart attribute
	chartConfig_2 = OrderedDict()
	chartConfig_2["caption"] = "Humidity"
	chartConfig_2["yAxisName"] = "Humidity (Percent)"
	chartConfig_2["xAxisName"] = "Time (seconds since launch)"
	#chartConfig_2["xaxismaxvalue"] = "60"
	#chartConfig_2["xaxisminvalue"] = "0"
	chartConfig_2["yaxismaxvalue"] = "100"
	chartConfig_2["theme"] = "ocean"

	dataSource_2["chart"] = chartConfig_2
	dataSource_2["dataset"] = []
	
	datasetConfig_2 = OrderedDict()
	datasetConfig_2["drawline"] = "1"
	#datasetConfig_2["seriesname"] = "Server 1"
	#datasetConfig_2["color"] = "#127fcb"
	datasetConfig_2["anchorsides"] = "3"
	datasetConfig_2["anchorradius"] = "8"
	#datasetConfig_2["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_2["anchorbordercolor"] = "#127fcb"
	datasetConfig_2["data"] = []
	
	#Iterate through the most recent 10 entries
	x = 0
	for key in humidity.objects.order_by('timestamp'):
		data = {}
		data["x"] = x
		data["y"] = key.humidity
		datasetConfig_2["data"].append(data)
		x = x + 10

	dataSource_2["dataset"].append(datasetConfig_2)
		
	# Create an object for the column 2D chart using the FusionCharts class constructor
	# The chart data is passed to the `dataSource` parameter.			
	humidityChart = FusionCharts("selectscatter", "ex2", 700, 400, "chart-2", "json", dataSource_2)
	
	# --------------------------- ALTITUDE ---------------------------

	#Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
	dataSource_3 = OrderedDict()

	# The `chartConfig` dict contains key-value pairs of data for chart attribute
	chartConfig_3 = OrderedDict()
	chartConfig_3["caption"] = "Altitude"
	chartConfig_3["yAxisName"] = "Altitude (Feet)"
	chartConfig_3["xAxisName"] = "Time (seconds since launch)"
	#chartConfig_3["xaxismaxvalue"] = "60"
	#chartConfig_3["xaxisminvalue"] = "0"
	#chartConfig_3["yaxismaxvalue"] = "100"
	chartConfig_3["theme"] = "ocean"

	dataSource_3["chart"] = chartConfig_3
	dataSource_3["dataset"] = []
	
	datasetConfig_3 = OrderedDict()
	datasetConfig_3["drawline"] = "1"
	#datasetConfig_3["seriesname"] = "Server 1"
	#datasetConfig_3["color"] = "#127fcb"
	datasetConfig_3["anchorsides"] = "3"
	datasetConfig_3["anchorradius"] = "8"
	#datasetConfig_3["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_3["anchorbordercolor"] = "#127fcb"
	datasetConfig_3["data"] = []
	
	#Iterate through the most recent 10 entries
	x = 0
	for key in location.objects.order_by('timestamp'):
		data = {}
		data["x"] = x
		data["y"] = key.altitude
		datasetConfig_3["data"].append(data)
		x = x + 10

	dataSource_3["dataset"].append(datasetConfig_3)
		
	# Create an object for the column 2D chart using the FusionCharts class constructor
	# The chart data is passed to the `dataSource` parameter.	
	altitudeChart = FusionCharts("selectscatter", "ex3", 700, 400, "chart-3", "json", dataSource_3)

	# --------------------------- ACCELERATION ---------------------------

	#Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
	dataSource_4 = OrderedDict()

	# The `chartConfig` dict contains key-value pairs of data for chart attribute
	chartConfig_4 = OrderedDict()
	chartConfig_4["caption"] = "Acceleration"
	chartConfig_4["yAxisName"] = "Acceleration (m/s^2)"
	chartConfig_4["xAxisName"] = "Time (seconds since launch)"
	#chartConfig_4["xaxismaxvalue"] = "60"
	#chartConfig_4["xaxisminvalue"] = "0"
	#chartConfig_4["yaxismaxvalue"] = "100"
	chartConfig_4["theme"] = "ocean"

	dataSource_4["chart"] = chartConfig_4
	dataSource_4["dataset"] = []
	
	# X - direction
	datasetConfig_x_4 = OrderedDict()
	datasetConfig_x_4["drawline"] = "1"
	datasetConfig_x_4["seriesname"] = "X"
	#datasetConfig_x_4["color"] = "#127fcb"
	datasetConfig_x_4["anchorsides"] = "3"
	datasetConfig_x_4["anchorradius"] = "8"
	#datasetConfig_x_4["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_x_4["anchorbordercolor"] = "#127fcb"
	datasetConfig_x_4["data"] = []
	
	# Y - direction
	datasetConfig_y_4 = OrderedDict()
	datasetConfig_y_4["drawline"] = "1"
	datasetConfig_y_4["seriesname"] = "Y"
	#datasetConfig_y_4["color"] = "#127fcb"
	datasetConfig_y_4["anchorsides"] = "3"
	datasetConfig_y_4["anchorradius"] = "8"
	#datasetConfig_y_4["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_y_4["anchorbordercolor"] = "#127fcb"
	datasetConfig_y_4["data"] = []
	
	# Z - direction
	datasetConfig_z_4 = OrderedDict()
	datasetConfig_z_4["drawline"] = "1"
	datasetConfig_z_4["seriesname"] = "Z"
	#datasetConfig_z_4["color"] = "#127fcb"
	datasetConfig_z_4["anchorsides"] = "3"
	datasetConfig_z_4["anchorradius"] = "8"
	#datasetConfig_z_4["anchorbgcolor"] = "#d3f7ff"
	#datasetConfig_z_4["anchorbordercolor"] = "#127fcb"
	datasetConfig_z_4["data"] = []
	
	#Iterate through the most recent 10 entries
	x = 0
	for key in acceleration.objects.order_by('timestamp'):
		data_x = {}
		data_x["x"] = x
		data_x["y"] = key.x_accel
		datasetConfig_x_4["data"].append(data_x)
		data_y = {}
		data_y["x"] = x
		data_y["y"] = key.y_accel
		datasetConfig_y_4["data"].append(data_y)
		data_z = {}
		data_z["x"] = x
		data_z["y"] = key.z_accel
		datasetConfig_z_4["data"].append(data_z)
		x = x + 10

	dataSource_4["dataset"].append(datasetConfig_x_4)
	dataSource_4["dataset"].append(datasetConfig_y_4)
	dataSource_4["dataset"].append(datasetConfig_z_4)
		
	# Create an object for the column 2D chart using the FusionCharts class constructor
	# The chart data is passed to the `dataSource` parameter.		
	accelerometerChart = FusionCharts("selectscatter", "ex4", 700, 400, "chart-4", "json", dataSource_4)

	# Images test code
	my_gallery = get_object_or_404(gallery, pk = 1)
	
	return render(request, 'data.html', {
		'output': temperatureChart.render(),
		'output2': humidityChart.render(),
		'output3': altitudeChart.render(),
		'output4': accelerometerChart.render(),
		'obj1' : my_gallery
	})
	
# Gallery Page
def gallery_data(request):

	# Images test code
	my_gallery = get_object_or_404(gallery, pk = 1)
	
	return render(request, 'gallery.html', {
		'obj1' : my_gallery
	})