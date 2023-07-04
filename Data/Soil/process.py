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
# Global Soil Maps: Global Soil Organic Carbon Density in kg Carbon/m2 to 1 meter depth
#def run_curl(url, output_file):
#    command = ['curl', '--user-agent', '--auth-no-challenge', '--user-agent', 'imajinarts14:junior$$14', url, '--output', output_file]
#    try:
#        subprocess.check_output(command)
#        print(f"File downloaded successfully as '{output_file}'")
#    except subprocess.CalledProcessError as e:
#        print(f"Error executing curl command: {e}")

# Usage
#url = "https://databasin2-filestore.s3.amazonaws.com/a4cb6d367eae4e52a08902874f8bfedf/download/a4cb6d367eae4e52a08902874f8bfedf_1_zip_en.zip?Signature=UioyS5g4XCL3ObjLT9xgJ3ecfdE%3D&Expires=1686983266&AWSAccessKeyId=AKIAI4RK5BEPK3FCQPUQ"
#output_file = "Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip"
#run_curl(url, output_file)

#zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').extractall()

#zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').close()

#gdalwarp_cmd = 'gdalwarp -to SRC_METHOD=NO_GEOTRANSFORM -s_srs EPSG:4326 -t_srs EPSG:4326 -tr 0.5 0.5 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "data/commonData\Data0\soilcarbon.ovr" "GlobalSoilOrganicCarbonDensityinkgCarbon_m2to1meterdepth.tif"'
#os.system(gdalwarp_cmd)

# Harmonized World Soil Database (HWSD)
wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/HWSD_Data/HWSD_RASTER.zip')

zipfile.ZipFile('HWSD_RASTER.zip').extractall()

zipfile.ZipFile('HWSD_RASTER.zip').close()

gdalwarp2_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -t_srs EPSG:4326 -tr 0.005 0.005 -r near -of GTiff -multi "hwsd.bil" "hwsd.tif"'
os.system(gdalwarp2_cmd)

# Soil Qualities for Crop Production HWSD Supplement
wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq1.asc')
gdalwarp3_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq1.asc" "sq1.tif"'
os.system(gdalwarp3_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq2.asc')
gdalwarp4_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq2.asc" "sq2.tif"'
os.system(gdalwarp4_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq3.asc')
gdalwarp5_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq3.asc" "sq3.tif"'
os.system(gdalwarp5_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq4.asc')
gdalwarp6_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq4.asc" "sq4.tif"'
os.system(gdalwarp6_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq5.asc')
gdalwarp7_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq5.asc" "sq5.tif"'
os.system(gdalwarp7_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq6.asc')
gdalwarp8_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq6.asc" "sq6.tif"'
os.system(gdalwarp8_cmd)

wget.download('http://webarchive.iiasa.ac.at/Research/LUC/External-World-soil-database/Soil_Quality/sq7.asc')
gdalwarp9_cmd = 'gdalwarp -t_srs EPSG:4326 -tr 0.05 0.05 -r near -of GTiff "sq7.asc" "sq7.tif"'
os.system(gdalwarp9_cmd)

# Global Organic Carbon GSOCmap VERSION 1.5.0
#wget.download('https://storage.googleapis.com/fao-maps-catalog-data/geonetwork/gsoc/GSOCmap/GSOCmap1.5.0.tif')
#gdalwarp10_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -t_srs EPSG:4326 -tr 0.005 0.005 -tap -te -180 -90 180 90 -r near -of GTiff -multi "GSOCmap1.5.0.tif" "Gsocmap1.5.0.tif"'
#os.system(gdalwarp10_cmd)

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[85] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-07-04 02-11-42.558752