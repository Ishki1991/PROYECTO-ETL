#!/usr/bin/env python
# coding: utf-8

# In[1]:


mi_ciudad = "Madrid"
ciudad = "Barcelona"
otra_ciudad = "Bilbao"


# In[2]:


#  Ya tengo mi df inicial. Busco datos para enriquecerlo
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# ciudad Barcelona
location_ciudad = geolocator.geocode(ciudad)
lat_ciudad = location_ciudad.latitude
long_ciudad = location_ciudad.longitude

# mi ciudad Madrid
location_mi_ciudad = geolocator.geocode(mi_ciudad)
lat_mi_ciudad = location_mi_ciudad.latitude
long_mi_ciudad = location_mi_ciudad.longitude

# otra ciudad Bilbao
location_otra_ciudad = geolocator.geocode(otra_ciudad)
lat_otra_ciudad = location_otra_ciudad.latitude
long_otra_ciudad = location_otra_ciudad.longitude


print("Latitud de ", mi_ciudad, ":" ,lat_mi_ciudad)
print("Longitud de ", mi_ciudad, ":" ,long_mi_ciudad)
print("Latitud de ", ciudad,":" ,lat_ciudad)
print("Longitud de ", ciudad,":" ,long_ciudad)
print("Latitud de ", otra_ciudad,":" ,lat_otra_ciudad)
print("Longitud de ", otra_ciudad,":" ,long_otra_ciudad)


# In[3]:


from datetime import datetime
from meteostat import Point, Daily

# Set time period
start = datetime(2018, 1, 1)
end = datetime(2022, 12, 31)

#Datos Barcelona
location_ciudad = Point(lat_ciudad,long_ciudad)

data_ciudad = Daily(location_ciudad, start, end)
data_ciudad = data_ciudad.fetch().reset_index()

#Datos Madrid
location_mi_ciudad = Point(lat_mi_ciudad,long_mi_ciudad)

data_mi_ciudad = Daily(location_mi_ciudad, start, end)
data_mi_ciudad = data_mi_ciudad.fetch().reset_index()

#Datos Bilbao
location_otra_ciudad = Point(lat_otra_ciudad,long_otra_ciudad)

data_otra_ciudad = Daily(location_otra_ciudad, start, end)
data_otra_ciudad = data_otra_ciudad.fetch().reset_index()

