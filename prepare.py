#1)Use the function defined in `aquire.py` to load the iris data.

import pandas as pd
import numpy as np
import scipy as sp 

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


def rename_columns(df):
    df['species']=df['species_name']
    return df

def split(df, target, train_prop, seed):
    return train_test_split(df, train_size=train_prop, stratify=df[target], random_state=seed)

def impute(train, test, my_strategy, column_list):
    imputer = SimpleImputer(strategy=my_strategy)
    train[column_list] = imputer.fit_transform(train[column_list])
    test[column_list] = imputer.transform(test[column_list])
    return train, test, imputer

def encode(train, test, col_name):
    encoded_values = sorted(list(train[col_name].unique()))
    
    # Integer Encoding
    int_encoder = LabelEncoder()
    train.encoded = int_encoder.fit_transform(train[col_name])
    test.encoded = int_encoder.transform(test[col_name])
    
    # create 2D np arrays of the encoded variable (in train and test)
    train_array = np.array(train.encoded).reshape(len(train.encoded),1)
    test_array = np.array(test.encoded).reshape(len(test.encoded),1)

    # One Hot Encoding
    ohe = OneHotEncoder(sparse=False, categories='auto')
    train_ohe = ohe.fit_transform(train_array)
    test_ohe = ohe.transform(test_array)
    
    # Turn the array of new values into a data frame with columns names being the values
    # and index matching that of train/test
    # then merge the new dataframe with the existing train/test dataframe
    train_encoded = pd.DataFrame(data=train_ohe,
                            columns=encoded_values, index=train.index)
    train = train.join(train_encoded)
    test_encoded = pd.DataFrame(data=test_ohe,
                               columns=encoded_values, index=test.index)
    test = test.join(test_encoded)
    return train, test, int_encoder, ohe

def scale_minmax(train, test, column_list):
    scaler = MinMaxScaler()
    column_list_scaled = [col + '_scaled' for col in column_list]
    train_scaled = pd.DataFrame(scaler.fit_transform(train[column_list]), 
                                columns = column_list_scaled, 
                                index = train.index)
    train = train.join(train_scaled)
    test_scaled = pd.DataFrame(scaler.transform(test[column_list]), 
                                columns = column_list_scaled, 
                                index = test.index)
    test = test.join(test_scaled)
    return train, test, scaler

def prepare(df, drop_cols, target, train_prop, seed, impute_cols, impute_strategy, encode_col, scale_cols):
    df.fillna(np.nan, inplace=True)
    df.drop(columns=drop_cols, inplace=True)
    train, test = split(df=df, target=target, train_prop=train_prop, seed=seed)
    train, test, imputer = impute(train, test, my_strategy=impute_strategy, column_list=impute_cols)
    train, test, int_encoder, ohe = encode(train, test, col_name = encode_col)
    train, test, scaler = scale_minmax(train, test, column_list = scale_cols)
    return df, train, test, imputer, int_encoder, ohe, scaler


def prep_telco(df):
    df['churn'] = df['churn'].replace({'Yes':1,'No':0})
    df['total_charges'] = df.total_charges.replace(' ', '0')
    df['total_charges'] = df.total_charges.astype('float')

    return df

def encode_variable(column):
    lab_enc = LabelEncoder()
    lab_enc.fit(df[column])
    df[column] = lab_enc.transform(df[column])

def encode_variable(column):
    lab_enc = LabelEncoder()
    lab_enc.fit(df[column])
    df[column] = lab_enc.transform(df[column])

def change_values(df):
    df['partner'] = df['partner'].replace({'Yes':1,'No':0})
    df['dependents'] = df['dependents'].replace({'Yes':1,'No':0})
    df['phone_service']= df ['phone_service'].replace({'Yes':1,'No':0})
    df['online_security']= df['online_security'].replace({'Yes':1,'No':0,'No internet service':2})
    df['device_protection']= df['device_protection'].replace({'Yes':1,'No':0,'No internet service':2})
    df['tech_support']= df['tech_support'].replace({'Yes':1,'No':0,'No internet service':2})
    df['streaming_tv']= df['streaming_tv'].replace({'Yes':1,'No':0,'No internet service':2})
    df['streaming_movies']= df['streaming_movies'].replace({'Yes':1,'No':0,'No internet service':2})
    df['paperless_billing']=df['paperless_billing'].replace({'Yes':1,'No':0})
    df['gender']= df['gender'].replace({'Male':1,'Female':0})
    df['contract_type']= df['contract_type'].replace({'Month-to-month':0,'One year':1,'Two year':2})
    #df['internet_service_type']=df['internet_service_type].replace({'none':0, })
    return df

