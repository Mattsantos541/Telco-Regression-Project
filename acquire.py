import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import split_scale
from sklearn.preprocessing import StandardScaler, MinMaxScaler
#import wrangle
import env
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


def get_db_url(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

url = get_db_url('telco_churn')
def prep_telco():
    df = pd.read_sql( """
    select *
    from customers
    join contract_types on customers.`contract_type_id`=`contract_types`.`contract_type_id`
    join `internet_service_types` on customers.`internet_service_type_id` = `internet_service_types`.`internet_service_type_id`
    join `payment_types` on customers.`payment_type_id` = `payment_types`.`payment_type_id`;""", url)

    return df

def prep_telco_month():
    df=pd.read_sql('''
    select *
    from customers
    join contract_types on customers.`contract_type_id`=`contract_types`.`contract_type_id`
    join `internet_service_types` on customers.`internet_service_type_id` = `internet_service_types`.`internet_service_type_id`
    join `payment_types` on customers.`payment_type_id` = `payment_types`.`payment_type_id`
    where `contract_type`= 'Month-to-month'
    ;''', url)

    return df

def prep_telco_1year():
      df=pd.read_sql('''
      select *
      from customers
      join contract_types on customers.`contract_type_id`=`contract_types`.`contract_type_id`
      join `internet_service_types` on customers.`internet_service_type_id` = `internet_service_types`.`internet_service_type_id`
      join `payment_types` on customers.`payment_type_id` = `payment_types`.`payment_type_id`
      where contract_type= 'One year';''', url)
      return df
  
