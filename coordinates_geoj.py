#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:19:53 2021

@author: daniela
"""

import folium
import geopandas as gpd
import webbrowser
import pandas as pd
import cv2 as cv
import os

path_img = '' #path of image
path_img_text = os.path.join(os.path.dirname(os.path.abspath(__name__)),"toponimos.csv") #path of text's points
path_images = os.path.join(os.path.dirname(os.path.abspath(__name__)),'IMAGENES_JPG')


df_imgtext = pd.read_csv(path_img_text) #df of text detected's points
df_imgtext['image'] = df_imgtext['imagen'].str.split('.', n=1, expand=True)[0]

all_country = gpd.read_file("Cob_Clasificacion_Analoga.json", driver = "GeoJSON")

vuelo = 'C-1256' #all_country['No_Vuelo']
foto = 328 #all_country['No_foto']
geoj = all_country

def geobound(geoj):
    '''
    Extract bounds from each foto
    '''
    coords = row['geometry'].bounds
    east, north = float(coords['maxx']), float(coords['maxy'])
    west, south = float(coords['minx']), float(coords['miny'])
    
    return east, north, west, south

east, north, west, south = geobound(vuelo,foto,geoj)


df_bounds = geoj
df_bounds[['west', 'south','east', 'north']] = geoj['geometry'].bounds
df_bounds.head()





img = 'C-1256_F-328'
im = cv.imread(os.path.join(path_images, img + '.jpg'),1) #uploing image
h, w, c = im.shape #shape of image, height, width and channels
df_img = df_imgtext[df_imgtext['image'] == img] #filtering texts for img

for row in df_img.index:
    'longitudes'
    point_0 = df_img.loc[row, '0'] #pixel 0 width - longitude
    lon_text = west + ((abs(west-east)/w)*point_0)
    'latitudes'
    point_1 = df_img.loc[row, '1'] #pixel 0 heigth - latitude
    lat_text = north - ((abs(north-south)/h)*point_1)
        
    df_img.loc[row, 'lon_text'] = lon_text.copy() #Add calculated longitude
    df_img.loc[row, 'lat_text'] = lat_text.copy() #Add calculated latitude

