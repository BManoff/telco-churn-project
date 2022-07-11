import pandas as pd
import numpy as np
import os
import env

# connect to the mysql server
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_telco_data():
    # Get local cached file if it's there
    filename = "telco_churn.csv" 

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('select * FROM customers JOIN contract_types using (contract_type_id) JOIN internet_service_types using (internet_service_type_id) JOIN payment_types using (payment_type_id)', get_connection('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  