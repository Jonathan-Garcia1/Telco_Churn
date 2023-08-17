import pandas as pd

from sklearn.model_selection import train_test_split
from acquire import get_telco_data


def drop_telco(df):

    return df.drop(columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])

def fillna_telco(df):
    df['internet_service_type'] = df['internet_service_type'].fillna("No internet service")
    return df

def dummies_telco(df):
    df = pd.get_dummies(df)
    df = df.drop(columns= ['gender_Female', 'partner_No', 'dependents_No', 'phone_service_No', 'multiple_lines_No', 
                            'multiple_lines_No phone service', 'online_security_No', 'online_security_No internet service', 
                            'online_backup_No', 'online_backup_No internet service', 'device_protection_No', 'device_protection_No internet service', 
                            'tech_support_No', 'tech_support_No internet service', 'streaming_tv_No', 'streaming_tv_No internet service', 
                            'streaming_movies_No', 'streaming_movies_No internet service', 'paperless_billing_No', 'churn_No', 
                            'internet_service_type_No internet service'])
    return df

def rename_telco(df):
    column_mapping = {
        'senior_citizen': 'senior_citizen',
        'tenure': 'tenure',
        'monthly_charges': 'monthly_charges',
        'total_charges': 'total_charges',
        'gender_Male': 'Male',
        'partner_Yes': 'partner',
        'dependents_Yes': 'dependents',
        'phone_service_Yes': 'phone_service',
        'multiple_lines_Yes': 'multiple_lines',
        'online_security_Yes': 'online_security',
        'online_backup_Yes': 'online_backup',
        'device_protection_Yes': 'device_protection',
        'tech_support_Yes': 'tech_support',
        'streaming_tv_Yes': 'streaming_tv',
        'streaming_movies_Yes': 'streaming_movies',
        'paperless_billing_Yes': 'paperless_billing',
        'churn_Yes': 'churn',
        'contract_type_Month-to-month': 'Contract Month',
        'contract_type_One year': 'Contract One year',
        'contract_type_Two year': 'Contract Two year',
        'internet_service_type_DSL': 'internet DSL',
        'internet_service_type_Fiber optic': 'internet Fiber optic',
        'payment_type_Bank transfer (automatic)': 'payment Bank transfer',
        'payment_type_Credit card (automatic)': 'payment Credit card',
        'payment_type_Electronic check': 'payment Electronic check',
        'payment_type_Mailed check': 'payment Mailed check'
    }

    # Rename the columns using the mapping
    df.rename(columns=column_mapping, inplace=True)

    # Print the new column names
    return df

def telco_train_val_test(df, strat, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed,
                                       stratify = df[strat])
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed,
                                 stratify = val_test[strat])
    
    return train, val, test




def telco_pipeline():

    df = get_telco_data()

    df = drop_telco(df)
    
    df = fillna_telco(df)

    df = dummies_telco(df)

    df = rename_telco(df)

    train, val, test = telco_train_val_test(df, 'churn')
    
    return train, val, test

def telco_work():

    df = get_telco_data()

    df = drop_telco(df)



    return df