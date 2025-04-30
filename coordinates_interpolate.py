# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:27:35 2021

@author: daniela.velasquez
"""

import pandas as pd
import os
import re
import json
import cv2 as cv

path_geoloc = os.path.join(os.path.dirname(os.path.abspath(__name__)),"geolocations.csv") #path of image geolocalizations 
path_imgtext = os.path.join(os.path.dirname(os.path.abspath(__name__)),"preliminar_terminado.csv") #path of text's points

df_imgtext = pd.read_csv(path_imgtext) #df of text's points
df_imgtext['image'] = df_imgtext['imagen'].str.split('.', n=1, expand=True)[0]
df_geoloc = pd.read_csv(path_geoloc) #df with geolocations
#df_geoloc = df_geoloc.rename(columns = {'Unnamed: 0':'image'}) #Cambio de nombre de la columna

path_images = os.path.join(os.path.dirname(os.path.abspath(__name__)),'IMAGENES_JPG\\Aerofotografias')

#with open(path_geoloc, 'r', encoding='utf-8') as jsonfile:
#    dict_geoloc = json.load(jsonfile)

df_geotext = pd.DataFrame({})

for i in df_geoloc.index: #loop over available images
    img = df_geoloc.loc[i,'filename']
    #coordinates of image
    north, south = df_geoloc.loc[i,'north'], df_geoloc.loc[i,'south']
    west, east = df_geoloc.loc[i,'west'], df_geoloc.loc[i,'east']
    df_img = df_imgtext[df_imgtext['image'] == img] #filtering texts for img
    im = cv.imread(os.path.join(path_images, img + '.jpg'),1)
    h, w, c = im.shape #shape of image, height, width and channels
    for row in df_img.index:
        'longitudes'
        point_w = df_img.loc[row, '0'] #pixel 0 widht - longitude
        lon_text = west + (((east - west)/w)*point_w) 
        
        'latitudes'
        point_h = df_img.loc[row, '1'] #pixel 0 hight - latitude
        lat_text = north + (((south - north)/h)*point_h)
         
        df_img.loc[row, 'lon_text'] = lon_text.copy() #Add calculated longitude
        df_img.loc[row, 'lat_text'] = lat_text.copy() #Add calculated latitude
    
    df_geotext = df_geotext.append(df_img)

df_geotext.to_csv('texts_geolocations.csv')   
    