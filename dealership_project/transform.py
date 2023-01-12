def transform_data(data):
    """This function round fuel price into two decimals """
    data['price'] = round(data.price, 2)
    return data
