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

csv_url = "https://opendata.arcgis.com/api/v3/datasets/e4bdbe8d6d8d4e32ace7d36a4aec7b93_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1"
csv_file = "Aboveground_Live_Woody_Biomass_Density.csv"
txt_file = csv_file.replace(".csv", ".txt")
folder_name = txt_file.replace(".txt", "")

# Download the CSV file
response = requests.get(csv_url)
with open(csv_file, 'wb') as file:
   file.write(response.content)

# Extract URLs from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    urls = [row["Mg_ha_1_download"] for row in reader]

# Create a folder with the same name as the text file
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save URLs in a TXT file
with open(txt_file, 'w') as file:
    file.write('\n'.join(urls))

# Read URLs from the text file
with open(txt_file, 'r') as file:
    urls = [line.strip() for line in file]

# Traverse the URLs and download the files
#for url in urls:
#    response = requests.get(url)
    # Extract the filename from the URL
#    filename = url.split('/')[-1]
#    filepath = os.path.join(folder_name, filename)
#    with open(filepath, 'wb') as file:
#        file.write(response.content)
#    print(f"Downloaded: {filename}")

for url in urls:
    # Extract the filename from the URL
    filename = url.split('/')[-1]
    filepath = os.path.join(folder_name, filename)

    # Use wget to download the file
    subprocess.run(['wget', '-O', filepath, url])

    print(f"Downloaded: {filename}")

# Set the directory where your files are located
directory = "Aboveground_Live_Woody_Biomass_Density"

# Get a list of files in the directory
files = os.listdir(directory)

# Iterate over the files
for file in files:
    # Use subprocess to execute the DVC add command
    subprocess.call(["dvc", "add", os.path.join(directory, file)])
    
    # Check if the file has the ".dvc" extension
    if file.endswith(".dvc"):
        # Use subprocess to execute the git add command
        subprocess.call(["git", "add", os.path.join(directory, file)])

# PanTropicalForestStrata
#AFR_strata
wget.download('https://glad.umd.edu/projects/pantropical/AFR_strata.zip')
zipfile.ZipFile('AFR_strata.zip').extractall()

zipfile.ZipFile('AFR_strata.zip').close()
gdalwarp2_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -s_srs EPSG:4326 -tr 0.00025 0.00025 -tap -r near -of GTiff -t_srs EPSG:4326 -multi -overwrite -co BIGTIFF=YES "AFR_strata.tif" "AFR_Strata.tif"'
os.system(gdalwarp2_cmd)

# SAM_strata
wget.download('https://glad.umd.edu/projects/pantropical/SAM_strata.zip')
zipfile.ZipFile('SAM_strata.zip').extractall()

zipfile.ZipFile('SAM_strata.zip').close()
gdalwarp3_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -s_srs EPSG:4326 -tr 0.00025 0.00025 -tap -r near -of GTiff -t_srs EPSG:4326 -multi -overwrite -co BIGTIFF=YES "SAM_strata.tif" "SAM_Strata.tif"'
os.system(gdalwarp3_cmd)

# SEA_strata
wget.download('https://glad.umd.edu/projects/pantropical/SEA_strata.zip')
zipfile.ZipFile('SEA_strata.zip').extractall()

zipfile.ZipFile('SEA_strata.zip').close()
gdalwarp4_cmd = 'gdalwarp -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 -s_srs EPSG:4326 -tr 0.00025 0.00025 -tap -r near -of GTiff -t_srs EPSG:4326 -multi -overwrite -co BIGTIFF=YES "SEA_strata.tif" "SEA_Strata.tif"'
os.system(gdalwarp4_cmd)

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[115] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-07-10 18-34-49.788428