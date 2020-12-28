import json
import pickle
import numpy as np
import os
__data_columns = None
__locations = None
__model = None


def get_estimated_price(location, sqft, size, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[1] = sqft
    x[2] = bath
    x[0] = size
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():

    global __data_columns
    global __locations



    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts")
    print(artifacts)
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    if __model is None:
        with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...start")

def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('Indira Nagar',1000, 2, 2))
