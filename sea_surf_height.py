# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cdsapi
import zipfile
import netCDF4 as nc4

c = cdsapi.Client()

dataset_name = 'reanalysis-oras5'
dict0 = {
            'format': 'zip',
            'product_type': 'consolidated',
            'vertical_resolution': 'single_level',
            'variable': 'sea_surface_height',
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12'
                ],
        }


for year in range(1958, 2014):
    
    dict0['year'] = year
    output = 'ssh_oras5_{}.zip'.format(year)
#    print(output)
    c.retrieve(dataset_name, dict0, output)
    
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(r"C:\Users\Professional\Downloads\pyLearn-master\pyLearn-master\ORAS5")
        
        
    obj = nc4.Dataset(output)
    ivars = {}
    for key in obj.variables:
        ivars[key] = obj.variables[key][:]
        
    time = obj.createDimension('time', 12)
    lat = obj.createDimension('lat', None)
    lon = obj.createDimension('lon', None)

    




