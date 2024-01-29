import sys
import os
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

# Get the Dataset and Process them
# Define the wget commands
wget_cmds = [
    # Global Soil Maps: Global Soil Organic Carbon Density in kg Carbon/m2 to 1 meter depth
    #'wget --auth-no-challenge --user=imajinarts14 --password=junior$$14 https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-global-gdb.zip',
    # Harmonized World Soil Database (HWSD)
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/HWSD_Data/HWSD_RASTER.zip',
    # Soil Qualities for Crop Production HWSD Supplement
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq1.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq2.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq3.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq4.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq5.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq6.asc',
    'wget http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq7.asc',
    # Global Organic Carbon GSOCmap VERSION 1.5.0
    #'wget https://storage.googleapis.com/fao-maps-catalog-data/geonetwork/gsoc/GSOCmap/GSOCmap1.5.0.tif'
]

# Execute the wget commands
for wget_cmd in wget_cmds:
    try:
        os.system(wget_cmd)
        print(f"Executed: {wget_cmd}")
    except Exception as e:
        print(f"Failed to execute {wget_cmd}: {str(e)}")

# unzip any zip files
def unzip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                    print(f"Extracted: {file_path}")

# Specify the directory you want to traverse and unzip files in
directory_to_traverse = "."

unzip_files(directory_to_traverse)

# Define the gdalwarp_cmd commands
gdalwarp_cmds = [
    # Global Soil Maps: Global Soil Organic Carbon Density in kg Carbon/m2 to 1 meter depth
    #'gdalwarp -to SRC_METHOD=NO_GEOTRANSFORM -s_srs EPSG:4326 -t_srs EPSG:4326 -tr 0.5 0.5 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "data/commonData\Data0\soilcarbon.ovr" "GlobalSoilOrganicCarbonDensityinkgCarbon_m2to1meterdepth.tif"',
    # Harmonized World Soil Database (HWSD)
    'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -t_srs EPSG:4326 -tr 0.005 0.005 -r near -of GTiff -multi "hwsd.bil" "hwsd.tif"',
    # Soil Qualities for Crop Production HWSD Supplement
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq1.asc" "sq1.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq2.asc" "sq2.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq3.asc" "sq3.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq4.asc" "sq4.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq5.asc" "sq5.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq6.asc" "sq6.tif"',
    'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq7.asc" "sq7.tif"',
    # Global Organic Carbon GSOCmap VERSION 1.5.0
    #'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -t_srs EPSG:4326 -tr 0.005 0.005 -tap -te -180 -90 180 90 -r near -of GTiff -multi "GSOCmap1.5.0.tif" "Gsocmap1.5.0.tif"'
]

# Execute the gdalwarp_cmd commands
for gdalwarp_cmd in gdalwarp_cmds:
    try:
        os.system(gdalwarp_cmd)
        print(f"Executed: {gdalwarp_cmd}")
    except Exception as e:
        print(f"Failed to execute {gdalwarp_cmd}: {str(e)}")

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[87] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2024-01-29 18-18-29.001967