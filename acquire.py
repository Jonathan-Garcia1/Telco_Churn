import os

import numpy as np
import pandas as pd

from env import get_connection

def get_db_connection(database):
    return get_connection(database)

def new_telco_data():
    sql_query = ('''
                 SELECT * 
                 FROM customers 
                 JOIN contract_types USING (contract_type_id) 
                 JOIN internet_service_types USING (internet_service_type_id) 
                 JOIN payment_types USING (payment_type_id)
                 ''')
    
    # Read in dataframe from Codeup db
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df

def get_telco_data():
    if os.path.isfile('telco.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
    else:
        # Read fresh data from db into a dataframe
        df = new_telco_data()
        # Cache data
        df.to_csv('telco.csv')
    return df   