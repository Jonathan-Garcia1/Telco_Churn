import pandas as pd

from sklearn.model_selection import train_test_split
from acquire import get_telco_data


def drop_telco(df):

    return df.drop(columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])

def name_telco(df):
    
    #print("Before renaming:", df.columns)
    
    # rename column to something more appropriate
    df = df.rename(columns={'payment_type': 'payment_method'})
    
    #print("After renaming:", df.columns)
    
    return df

def fix_types_telco(df):
    
    df['total_charges'] = df['total_charges'].replace(' ', 0).astype(float)
    
    return df

def fillna_telco(df):
    
    df['internet_service_type'] = df['internet_service_type'].fillna("No internet service")
    
    return df

def replace_telco(df):
    
    df['senior_citizen'] = df['senior_citizen'].replace({1: 'Yes', 0: 'No'})
    df['multiple_lines'] = df['multiple_lines'].replace('No phone service', 'No')
    df['online_security'] = df['online_security'].replace('No internet service', 'No')
    df['online_backup'] = df['online_backup'].replace('No internet service', 'No')
    df['device_protection'] = df['device_protection'].replace('No internet service', 'No')
    df['tech_support'] = df['tech_support'].replace('No internet service', 'No')
    df['streaming_tv'] = df['streaming_tv'].replace('No internet service', 'No')
    df['streaming_movies'] = df['streaming_movies'].replace('No internet service', 'No')
    df['payment_method'] = df['payment_method'].replace({
        'Credit card (automatic)': 'Credit card',
        'Bank transfer (automatic)': 'Bank transfer'
        })

    
    return df


def map_telco(df):
    
    # internet_service
    df['internet_service'] = df['internet_service_type'].map({
    'DSL': 'Yes',
    'Fiber optic': 'Yes',
    'No internet service': 'No'
    })
    
    # payment_type
    df['payment_type'] = df['payment_method'].map({
    'Mailed check': 'Manual',
    'Electronic check': 'Manual',
    'Credit card': 'Automatic',
    'Bank transfer': 'Automatic'
    })
    
    # Contract
    df['contract'] = df['contract_type'].map({
    'One year': 'Yes',
    'Two year': 'Yes',
    'Month-to-month': 'No'
    })


    return df


def reorder_telco(df):
    
    new_column_order = [
    'gender', 'senior_citizen', 'partner', 'dependents', 'tenure',
    'phone_service', 'multiple_lines', 'internet_service', 'internet_service_type', 'online_security', 'online_backup',
    'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract', 'contract_type', 'payment_method', 'payment_type',
    'paperless_billing', 'monthly_charges', 'total_charges', 'churn'
    ]   

    df = df[new_column_order]
    
    return df


def telco_train_val_test(df, strat, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed,
                                       stratify = df[strat])
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed,
                                 stratify = val_test[strat])
    
    return train, val, test


def dummies_telco(df):
    
    df = pd.get_dummies(df)
    
    keep_cols = ['tenure', 'monthly_charges', 'internet_service_type_DSL', 'internet_service_type_Fiber optic', 
             'internet_service_type_No internet service', 'payment_method_Bank transfer', 
             'payment_method_Credit card', 'payment_method_Electronic check', 'payment_method_Mailed check', 'churn_Yes']
    
    df = df[keep_cols]
    
    
    
    return df


def dummies_telcov2(df):
    
    df = pd.get_dummies(df)
    
    keep_cols = ['tenure', 'monthly_charges', 'gender_Male', 'senior_citizen_Yes',
            'partner_Yes', 'dependents_Yes', 'phone_service_Yes', 'multiple_lines_Yes', 
            'internet_service_Yes','internet_service_type_DSL', 'internet_service_type_Fiber optic',
            'internet_service_type_No internet service', 'tech_support_Yes', 'contract_Yes',
            'contract_type_One year', 'contract_type_Two year', 'payment_method_Bank transfer', 
            'payment_method_Credit card', 'payment_method_Electronic check', 'payment_method_Mailed check',
            'payment_type_Automatic', 'payment_type_Manual', 'paperless_billing_Yes', 'churn_Yes']  
    
    df = df[keep_cols]
    
    
    
    return df


def name_cols_telco(df):
    new_column_names = {
        'tenure': 'tenure',
        'monthly_charges': 'monthly_charges',
        'internet_service_type_DSL': 'internet_dsl',
        'internet_service_type_Fiber optic': 'internet_fiber_optics',
        'internet_service_type_No internet service': 'internet_no_internet',
        'payment_method_Bank transfer': 'payment_method_bank_transfer',
        'payment_method_Credit card': 'payment_method_credit_card',
        'payment_method_Electronic check': 'payment_method_electronic_check',
        'payment_method_Mailed check': 'payment_method_mailed_check',
        'churn_Yes': 'churn'
    }
    
    df.rename(columns=new_column_names, inplace=True)
    return df

def name_cols_telcov2(df):
    
    new_column_names = {
        'tenure': 'tenure',
        'monthly_charges': 'monthly_charges',
        'gender_Male': 'gender',
        'senior_citizen_Yes': 'senior_citizen',
        'partner_Yes': 'partner',
        'dependents_Yes': 'dependents',
        'phone_service_Yes': 'phone_service',
        'multiple_lines_Yes': 'multiple_lines',
        'internet_service_Yes': 'internet_service',
        'internet_service_type_DSL': 'internet_dsl',
        'internet_service_type_Fiber optic': 'internet_fiber_optic',
        'internet_service_type_No internet service': 'internet_no_internet',
        'tech_support_Yes': 'tech_support',
        'contract_Yes': 'contract',
        'contract_type_One year': 'contract_type_one_year',
        'contract_type_Two year': 'contract_type_two_year',
        'payment_method_Bank transfer': 'payment_method_bank_transfer',
        'payment_method_Credit card': 'payment_method_credit_card',
        'payment_method_Electronic check': 'payment_method_electronic_check',
        'payment_method_Mailed check': 'payment_method_mailed_check',
        'payment_type_Automatic': 'payment_type_automatic',
        'payment_type_Manual': 'payment_type_manual',
        'paperless_billing_Yes': 'paperless_billing',
        'churn_Yes': 'churn'
    }

    df.rename(columns=new_column_names, inplace=True)

# Example usage:
# name_cols_telco(your_dataframe)

    df.rename(columns=new_column_names, inplace=True)
    return df



def telco_prep():

    df = get_telco_data()
    
    df = name_telco(df)
    
    df = drop_telco(df)
    
    df = fix_types_telco(df)
    
    df = fillna_telco(df)
    
    df = replace_telco(df)
    
    df = map_telco(df)
    
    df = reorder_telco(df)
    
    return df

def telco_pipeline():
    
    df = get_telco_data()
    
    df = name_telco(df)
    
    df = drop_telco(df)
    
    df = fix_types_telco(df)
    
    df = fillna_telco(df)
    
    df = replace_telco(df)
    
    df = map_telco(df)
    
    df = reorder_telco(df)
    
    train, val, test = telco_train_val_test(df, 'churn')
    
    
    train = dummies_telco(train)
    
    train = name_cols_telco(train)
    
    
    val = dummies_telco(val)
    
    val = name_cols_telco(val)
    
    
    test = dummies_telco(test)
    
    test = name_cols_telco(test)
    
    
    return train, val, test

def split_telco(train, val, test):

    # Split data into predicting variables (X) and target variable (y) and reset the index for each dataframe
    train_X = train.drop(columns='churn').reset_index(drop=True)
    train_y = train.churn

    val_X = val.drop(columns='churn').reset_index(drop=True)
    val_y = val.churn

    test_X = test.drop(columns='churn').reset_index(drop=True)
    test_y = test.churn

    return train_X, val_X, test_X, train_y, val_y, test_y


def telco_modeling():
    
    df = get_telco_data()
    
    df = name_telco(df)
    
    df = drop_telco(df)
    
    df = fix_types_telco(df)
    
    df = fillna_telco(df)
    
    df = replace_telco(df)
    
    df = map_telco(df)
    
    df = reorder_telco(df)
    
    train, val, test = telco_train_val_test(df, 'churn')
    
    
    train = dummies_telco(train)
    
    train = name_cols_telco(train)
    
    
    val = dummies_telco(val)
    
    val = name_cols_telco(val)
    
    
    test = dummies_telco(test)
    
    test = name_cols_telco(test)
    
    train_X, val_X, test_X, train_y, val_y, test_y = split_telco(train, val, test)
    
    return train_X, val_X, test_X, train_y, val_y, test_y


def telco_modelingv2():
    
    df = get_telco_data()
    
    df = name_telco(df)
    
    df = drop_telco(df)
    
    df = fix_types_telco(df)
    
    df = fillna_telco(df)
    
    df = replace_telco(df)
    
    df = map_telco(df)
    
    df = reorder_telco(df)
    
    train, val, test = telco_train_val_test(df, 'churn')
    
    
    train = dummies_telcov2(train)
    
    train = name_cols_telcov2(train)
    
    
    val = dummies_telcov2(val)
    
    val = name_cols_telcov2(val)
    
    
    test = dummies_telcov2(test)
    
    test = name_cols_telcov2(test)
    
    train_X, val_X, test_X, train_y, val_y, test_y = split_telco(train, val, test)
    
    return train_X, val_X, test_X, train_y, val_y, test_y



def telco_work():

    df = get_telco_data()

    df = drop_telco(df)

    return df

