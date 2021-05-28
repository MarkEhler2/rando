import csv
import os
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

os.getcwd()
test_file = 'sfav2_CONUS_24h_2019100200.tif.csv'

imported_csvs = []
for fi in onlyfiles:
    if fi.endswith('.csv'):
        print(fi)
        _,_,_,date = fi.split('_')
        date = date.strip('.tif.csv')
        print(date)
        csv_file = csv.DictReader(open(test_file, 'r'), delimiter=',', quotechar='"')
        for row in csv_file:
            row[''] = date
            imported_csvs.append(row)
imported_csvs   
csv_file = "daily_snowfall_VT_counties.csv"
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=imported_csvs[0].keys())
        writer.writeheader()
        for data in imported_csvs:
            print(data)
            writer.writerow(data)
except IOError:
    print("I/O error")