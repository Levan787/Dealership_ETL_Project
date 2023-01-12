from log_message import log
from extract_data import extract
from transform import transform_data
from load import load
from configs.constants import targetfile, etl_started, extract_started, extract_ended, transform_started, \
    transform_ended, load_started, load_ended, etl_ended


def main():
    """ETL process"""
    log(etl_started)

    log(extract_started)
    extracted_data = extract()
    log(extract_ended)

    log(transform_started)
    transformed_data = transform_data(extracted_data)
    log(transform_ended)

    log(load_started)
    load(targetfile, transformed_data)
    log(load_ended)

    log(etl_ended)


if __name__ == '__main__':
    main()
