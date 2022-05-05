#This is a test of python script for parsing Louisville scooter data

#To do this , I will need to pull data from Lou Open Data Dockless Vehicles , Carto & OpenStreetsMap

#Jupyter Notebooks will be used to visualize data

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