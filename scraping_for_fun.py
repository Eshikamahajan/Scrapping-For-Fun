# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:56:41 2020

@author: Eshika Mahajan
"""
#----------------------------------------Learning 1-------------------------------------------
from urllib.request import urlopen
api_url="https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=439d4b804bc8187953eb36d2a8c26a02"

url_result=urlopen(api_url) #saving the HTTP response result of api_url
data=url_result.read() # type(data)==bytes

import json
json_data=json.loads(data)  #this is of type dictionary

#converting dictionary to strings
json_string=json.dumps(json_data)  # converted dictionary to string

import requests
#----------------------------------------Learning 2-------------------------------------------
'''

#---------------------------------------GOOGLE API

url="https://maps.googleapis.com/maps/api/geocode/json?"

parameters={'address':'your address here','key':'GIVE YOUR KEY HERE'}
r=requests.get(url,params=parameters)
r.url
print(r.content.decode('UTF-8'))

'''

#----------------------------------------Learning 3-------------------------------------------
fb_url='https://graph.facebook.com/4/picture?type=large'  #4 corresponds to zukerberg;s id
r=requests.get(fb_url)  #returns image
binary=r.content  # binary encoding if the image
#we will save this binary encodes into a file and then view the immage4

with open('Profile_pic.jpg','wb') as f:  
    
    f.write(binary)






