import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import split_scale
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import wrangle
import env
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler




url = env.get_db_url('iris_db')

def prep_iris():
    df = pd.read_sql("""
SELECT *
FROM measurements m
JOIN species s on s.species_id = m.species_id;
"""

,url)
    df.drop(['species_id','measurement_id'],axis=1,inplace=True)
    df.rename(columns={'species_name':'species'},inplace=True)
    int_encoder = LabelEncoder()
    int_encoder.fit(df.species)
    df.species = int_encoder.transform(df.species)


    return df