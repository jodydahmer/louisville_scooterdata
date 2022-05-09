#This is a test of python script for parsing Louisville scooter data

#To do this , I will need to pull data from Lou Open Data Dockless Vehicles , Carto & OpenStreetsMap

#Jupyter Notebooks will be used to visualize data

#TripID - a unique ID created by Louisville Metro
#StartDate - in YYYY-MM-DD format
#StartTime - rounded to the nearest 15 minutes in HH:MM format
#EndDate - in YYYY-MM-DD format
#EndTime - rounded to the nearest 15 minutes in HH:MM format
#TripDuration - duration of the trip minutes
#TripDistance - distance of trip in miles based on company route data
#StartLatitude - rounded to nearest 3 decimal places
#StartLongitude - rounded to nearest 3 decimal places
#EndLatitude - rounded to nearest 3 decimal places
#EndLongitude - rounded to nearest 3 decimal places
#DayOfWeek - 1-7 based on date, 1 = Sunday through 7 = Saturday, useful for analysis
#HourNum - the hour part of the time from 0-24 of the StartTime, useful for analysis

!pip install osm-runner


import time

from osm_runner import Runner  # pip install osm-runner
import pandas as pd

from arcgis.features import FeatureLayer, GeoAccessor, GeoSeriesAccessor
from arcgis.geoenrichment import enrich
from arcgis import dissolve_boundaries
from arcgis.geometry import project
from arcgis.gis import GIS

# Organization Login
gis = GIS('home')

