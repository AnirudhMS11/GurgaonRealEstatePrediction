import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None
__property_types = None

def get_Price(bhk,area,prop_type,loc):
        loc = loc.lower()
        input_vector = np.zeros(len(__data_columns))
        col_index_map = {col: idx for idx, col in enumerate(__data_columns)}
        if 'BEDROOM_NUM' in col_index_map:
            input_vector[col_index_map['BEDROOM_NUM']] = bhk
        if 'AREA' in col_index_map:
            input_vector[col_index_map['AREA']] = area
        prop_col = f'PROPERTY_TYPE_{prop_type}'
        if prop_col in col_index_map:
            input_vector[col_index_map[prop_col]] = 1
        loc_col = f'location_{loc}'
        if loc_col in col_index_map:
            input_vector[col_index_map[loc_col]] = 1
        input_df = pd.DataFrame([input_vector], columns=__data_columns)
        
        return round(__model.predict(input_df)[0],2)

def clean_location_properties():
       global __locations
       global __property_types

       __property_types = [ptype.replace("PROPERTY_TYPE_","") for ptype in __property_types]
       __locations = [loc.replace("location_","") for loc in __locations]

       print("Property Types and Locations are cleaned")
       

def get_locations():
    return __locations

def get_property_type():
        return __property_types

def load_artifacts():
        print("Loading artifacts")
        global __data_columns
        global __locations
        global __model
        global __property_types

        with open("./artifacts/columns.json",'r') as f:
                __data_columns = json.load(f)['data_columns']
                __locations = __data_columns[4:]
                __property_types = __data_columns[2:4]

        with open("./artifacts/GRM.pickle",'rb') as f:
                __model = pickle.load(f)
                print(__model)

        clean_location_properties()

        print("Loaded Artifacts")

if __name__ == '__main__':
    load_artifacts()
    print(get_property_type())
    print(get_locations())
    print(get_Price(2,1400,'Residential Apartment','other'))
    print(get_Price(3,1800,'Independent/Builder Floor','sector 82 gurgaon'))
