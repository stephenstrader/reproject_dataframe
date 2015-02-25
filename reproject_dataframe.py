# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:48:14 2015
Last modified on Wed Feb 25 2015
@author: StephenStrader

Purpose: Reada shapefile with geopandas as a dataframe and reproject the 
         shapefile.  
"""
import geopandas as gpd

#data source (http://www.spc.noaa.gov/gis/svrgis/) (tornado.zip)
shapefile='C:\\Users\\StephenStrader\\Desktop\\reproject_dataframe\\tornado.shp'

#read shapefile as GeoDataFrame and reproject to WGS84 (EPSG = 4326)
StormData = gpd.GeoDataFrame.from_file(shapefile).to_crs(epsg=4326) 



