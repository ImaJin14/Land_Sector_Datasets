import sys
import os
import subprocess
import csv
import requests
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])


# Global Forest Maps: Global forest management data for 2015 at a 100 m resolution
wget.download('https://zenodo.org/record/5879022/files/FML_v3-2_with-colorbar.tif?download=1')
gdalwarp1_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -t_srs EPSG:4326 -tr 0.01 0.01 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "FML_v3-2_with-colorbar.tif" "GlobalForestManagementData_at_a_100m_resolution.tif"'
os.system(gdalwarp1_cmd)

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[27] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-07-07 18-38-15.405065