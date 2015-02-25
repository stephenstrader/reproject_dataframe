# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:48:14 2015
Last modified on Wed Feb 25 2015
@author: StephenStrader

Purpose: Reada shapefile with geopandas as a dataframe and reproject the 
         shapefile.  
"""
import geopandas as gpd

shapefile='C:\\Users\\StephenStrader\\Desktop\\reproject_dataframe\\tornado.shp'

StormData = gpd.read_file(shapefile).to_crs(epsg=4326) #EPSG for WGS84 = 4326



