import sys
import subprocess
import wget
import zipfile
import datetime
import os


# Download the zip file
# Define the wget commands
wget_cmds = [
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-global-gdb.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-africa-shp.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-asia-shp.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-europe-shp.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-americas-shp.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-oceania-east-shp.zip',
    'wget --auth-no-challenge --user=Simpleshell --password=9KvEve-X_F.jmxV https://sedac.ciesin.columbia.edu/downloads/data/groads/groads-global-roads-open-access-v1/groads-v1-oceania-west-shp.zip'
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

# Processing shapefiles to json 
gdalwarp0_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-global.json" "groads-v1-global-gdb/groads-v1-global.gdb"'
os.system(gdalwarp0_cmd)

gdalwarp1_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "gROADS-v1-africa.json" "groads-v1-africa-shp/gROADS-v1-africa.shp"'
os.system(gdalwarp1_cmd)

gdalwarp2_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-asia.json" "groads-v1-asia-shp/groads-v1-asia.shp"'
os.system(gdalwarp2_cmd)

gdalwarp3_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-europe.json" "groads-v1-europe-shp/groads-v1-europe.shp"'
os.system(gdalwarp3_cmd)

gdalwarp4_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-americas.json" "groads-v1-americas-shp/groads-v1-americas.shp"'
os.system(gdalwarp4_cmd)

gdalwarp5_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-oceania-east.json" "groads-v1-oceania-east-shp/groads-v1-oceania-east.shp"'
os.system(gdalwarp5_cmd)

gdalwarp6_cmd = 'ogr2ogr -f GeoJSON -t_srs EPSG:4326 "groads-v1-oceania-west.json" "groads-v1-oceania-west-shp/groads-v1-oceania-west.shp"'
os.system(gdalwarp6_cmd)

# Update the "process.py" file with a timestamp
a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[74] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-07-28 13-58-27.972682