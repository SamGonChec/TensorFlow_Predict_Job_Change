# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

import tensorflow as tf
import pandas as pd
import tensorflow_datasets as tfds
from tensorflow import keras
from tensorflow.keras import layers
import pickle
import numpy as np

#I USED COLABS FOR THIS PROJECT SO THE PATHING MIGHT BE WEIRD!

#I followed the tutorial on the tensorflow site to learn how to upload dataframes: https://www.tensorflow.org/tutorials/load_data/pandas_dataframe 
# initialData = tf.keras.utils.get_file('aug_train.csv',)
#Sources for all my work here :
#get_dummies :https://stackoverflow.com/questions/37292872/how-can-i-one-hot-encode-in-python, https://stackoverflow.com/questions/59043662/create-a-new-column-in-pandas-dataframe-based-on-the-nan-values-in-other-colum
#renaming multiple columns:https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/ 
#drop columns: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

reader = pd.read_csv('/content/drive/MyDrive/CS461/aug_train.csv')
reader.head()

gender_encode = pd.get_dummies(reader['gender'],dummy_na=True)
reader = reader.drop('gender',axis=1)
gender_encode = gender_encode.rename(columns=str).rename(columns={'nan':'gender_null'})
reader = reader.join(gender_encode)
reader.head()

relevant_encode = pd.get_dummies(reader['relevent_experience'],dummy_na=True)
reader = reader.drop('relevent_experience',axis=1)
relevant_encode = relevant_encode.rename(columns=str).rename(columns={'nan':'relevent_null'})
reader = reader.join(relevant_encode)
reader.head()

enroll_encode = pd.get_dummies(reader['enrolled_university'],dummy_na=True)
reader = reader.drop('enrolled_university',axis=1)
enroll_encode = enroll_encode.rename(columns=str).rename(columns={'nan':'enrollment_null'})
reader = reader.join(enroll_encode)
reader.head()

education_encode = pd.get_dummies(reader['education_level'],dummy_na=True)
reader = reader.drop('education_level',axis=1)
education_encode = education_encode.rename(columns=str).rename(columns={'nan':'education_null'})
reader = reader.join(education_encode)
reader.head()

major_encode = pd.get_dummies(reader['major_discipline'],dummy_na=True)
reader = reader.drop('major_discipline',axis=1)
major_encode = major_encode.rename(columns=str).rename(columns={'Other':'other_major'})
major_encode = major_encode.rename(columns=str).rename(columns={'nan':'major_null'})
reader = reader.join(major_encode)
reader.head()

reader.replace({"experience": {
    ">20":    21,
    "<1": 0
}}, inplace=True)
reader.head()

company_encode = pd.get_dummies(reader['company_size'],dummy_na=True)
reader = reader.drop('company_size',axis=1)
company_encode = company_encode.rename(columns=str).rename(columns={'Other':'other_major'})
company_encode = company_encode.rename(columns=str).rename(columns={'nan':'company_size_null'})
reader = reader.join(company_encode)
reader.head()

company_type_encode = pd.get_dummies(reader['company_type'],dummy_na=True)
reader = reader.drop('company_type',axis=1)
company_type_encode = company_type_encode.rename(columns=str).rename(columns={'Other':'other_company_type'})
company_type_encode = company_type_encode.rename(columns=str).rename(columns={'nan':'company_type_null'})
reader = reader.join(company_type_encode)
reader.head()

reader.replace({"last_new_job": {
    "never":  0,
    ">4": 5,
}}, inplace=True)
reader['last_new_job'] = reader['last_new_job'].replace(np.nan, 0)
reader.to_csv('encoded_data.csv')
