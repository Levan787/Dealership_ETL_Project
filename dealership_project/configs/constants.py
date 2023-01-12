tmpfile = "dealership_temp.tmp"  # file used to store all extracted data
logfile = "dealership_logfile.txt"  # all event logs will be stored in this file
targetfile = "dealership_transformed_data.csv"  # file where transformed data is stored

car_model = "car_model"  # column names
year_of_manufacture = "year_of_manufacture"
price = "price"
fuel = "fuel"

csv_files = "dealership_data/*.csv"  # csv, json and xml files
json_files = "dealership_data/*.json"
xml_files = "dealership_data/*.xml"

etl_started = "ETL job started"  # ETL job
extract_started = "Extract phase started"
extract_ended = "Extract phase ended"
transform_started = "Transform phase started"
transform_ended = "Transform phase ended"
load_started = "Load phase started"
load_ended = "Load phase ended"
etl_ended = "ETL job ended"
