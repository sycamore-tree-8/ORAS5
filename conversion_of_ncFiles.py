# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:17:51 2021

@author: Professional
"""

import os 

import numpy as np 
import pandas as pd

import xarray as xr

import netCDF4 as nc4

import time as tm


files_path = '../'

lst = os.listdir(files_path)

nc_lst = sorted([x for x in lst if ('.nc' in x[-4:])]) 

#print(nc_lst)
    

for cyear in range(1958, 1963):
    
    annual_lst = sorted([y for y in nc_lst if ('{}'.format(cyear) in y[:])])

    start = True    
    for i, output in enumerate(annual_lst[:]):
        
        tm1 = tm.time()
        full_data_path = '{}/{}'.format(files_path, output)
        
        obj = nc4.Dataset(full_data_path)   
        ivars = obj.variables.keys()
        lons   = obj.variables['nav_lon'][:]
    #    obj.close()
        
    #    ds = xr.open_dataset(full_data_path)
    #    ivars = {}
    #    for key in ds.variables.keys():
    #        ivars[key] = ds.variables[key].values
       
       #  arr = obj.variables['sossheig'].values
       #  itime = obj.variables['time_counter'].values
        
       #  if start == True:
       #      box = arr[:]
       #      times = [itime[0]]
       #  else:
       #      box = np.concatenate((box, arr), axis=0)
       #      times.append(itime[0]) # np.concatenate((times, itime), axis=0)
            
    
       #  tm2 = tm.time()
       # # print('{}/{} {:.2f}'.format(i, len(nc_lst), tm2 - tm1))
        
       #  if i == 11:
       #      lons = obj.variables['nav_lon'].values
       #      lats = obj.variables['nav_lat'].values

       #  start = False

            
    # fileName = 'sshData_{}.nc'.format(cyear)
    # print(fileName)
       

    # obj = xr.Dataset(
    #     {"ssh": (("time", "lat", "lon" ), box),
    #      "lats": (("lat", "lon" ), lats),
    #      "lons": (("lat", "lon" ), lons),
    #      'times' : (("time"), times)
    #      },
    #     coords={
    #         "time": range(12),
    #         "lat": range(1021),
    #         "lon": range(1442),
    #     },
        
    #  )
    
    
    # obj.to_netcdf(fileName)
        
        