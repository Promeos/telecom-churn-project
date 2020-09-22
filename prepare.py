import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

from acquire import get_telecom_data

def telcom_data_prep(data_split=False):
    '''
    Load telco_data as a pandas DataFrame
    Clean numeric types and creates dummy variables
    '''
    
    # Call function to load the telco dataset
    df = get_telecom_data()
    
    # Clean and cast total_charges column from type object to float
    df.total_charges = df.total_charges.str.strip()
    
    # New customers that have recently signed up have value of ''. '' == 0 tenure and 0 total charges
    df.total_charges = df.total_charges.replace('', np.nan)  # Replace empty strings with np.nan
    df.total_charges = df.total_charges.astype("float")  # Cast the entire column from type string to float
    
    # Drop the observations where customers have not paid their first month with telco
    df.dropna(inplace=True)
    
    # Replace target variable strings('Yes'/'No') with int's(1/0)
    df.churn = np.where(df.churn == 'Yes', 1, 0)
    
    df['tenure_years'] = df.tenure / 12
    
    # Collect the column name where values are categorical/strings/objects
    encoded_columns = df.nunique()[df.nunique() <= 4].index.to_list()  # Columns with 4 or less unique values
    encoded_columns.remove('churn')  # remove churn from this list, we've already converted the values to binary outcomes
    encoded_attributes = pd.get_dummies(df[encoded_columns])  # with the remaining object columns, create dummy variables.
    
    df = pd.concat([df, encoded_attributes], axis=1)  # concat the original dataframe with the encoded attributes.
    
    encoded_columns.append('customer_id')  # append categorical columns with customer_id
    df.drop(columns=encoded_columns, inplace=True)  # drop all columns that are represented by pd.dummies
    churn = df.churn
    
    df.drop(columns='churn', inplace=True)
    df = pd.concat([df, churn], axis=1)

    return df
    
    # if data_split == True:
    #     return preprocessed_data()
    # elif data_split == False:
    #     return df
    # else:
    #     return None
   
# def preprocessed_data()
    # df = df_telecom_prep()
    
    # X = 
    # y = df
    
    # train_validate, test = train_test_split(


# def scale - iteration 2

