import pandas as pd  # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
import glob  # this module helps in selecting files

from configs.constants import car_model, year_of_manufacture, price, fuel, \
    csv_files, json_files, xml_files


def extract_from_csv(file_to_process):
    """read data form csv file"""
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    """read data from json file"""
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    """read data from xml file"""
    dataframe = pd.DataFrame(columns=[car_model, year_of_manufacture, price, fuel])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        car_model_value = person.find(car_model).text
        year_of_manufacture_value = int(person.find(year_of_manufacture).text)
        price_value = float(person.find(price).text)
        fuel_value = person.find(fuel).text
        dataframe = dataframe.append({car_model: car_model_value,
                                      year_of_manufacture: year_of_manufacture_value, price: price_value,
                                      fuel: fuel_value}, ignore_index=True)
        return dataframe


def extract():
    """extract data from csv, json and xml files togather"""
    extracted_data = pd.DataFrame(columns=[car_model, year_of_manufacture, price, fuel])  # create an empty data frame
    # to hold extracted data

    # process all csv files
    for csvfile in glob.glob(csv_files):
        extracted_data = pd.concat([extracted_data, extract_from_csv(csvfile)], ignore_index=True)
    # process all json files
    for jsonfile in glob.glob(json_files):
        extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)
    # process all xml files
    for xmlfile in glob.glob(xml_files):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xmlfile)], ignore_index=True)

    return extracted_data
