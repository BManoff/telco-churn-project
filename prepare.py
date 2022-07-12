from pydataset import data
import seaborn as sns
import pandas as pd
import acquire
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


def prep_telco_data():

    df = acquire.get_telco_data()
       
    # Droping white space  
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Converting total charges to a float
    df['total_charges'] = df.total_charges.astype(float)
    
    # Converting binary and catagorical to numeric
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    df['internet_service_encoded'] = df.internet_service_type.map({'None': 0, 'Fiber optic': 1, 'DSL': 2})
    df['contract_type_encoded'] = df.contract_type.map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    
    # Make dummy variables for catagorical columns
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=True)

 # Dropping unnecesary and ID columns
    df.drop(columns=['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'churn', 'gender', 
                    'partner', 'dependents', 'phone_service', 'paperless_billing', 'multiple_lines',
                    'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv',
                    'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type' ], inplace=True)


    # concats dummy to DF
    df = pd.concat([df, dummy_df], axis=1)
    return df

# generic splitting function
def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.churn_encoded
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.churn_encoded,
    )
    return train, validate, test


