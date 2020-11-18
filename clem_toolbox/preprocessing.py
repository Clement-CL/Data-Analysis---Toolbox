####### DATA PREPROCESSING #######
import pandas as pd

## MISSING VALUES
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

## ENCODERS
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def one_hot_encoding(df):
    df_cat = df.copy().select_dtypes(include=["object"])
    ohe = OneHotEncoder().fit(df_cat)
    transformed_array = ohe.transform(df_cat).toarray()
    categorical_data_ohe = pd.DataFrame(transformed_array, columns=ohe.get_feature_names(df_cat.columns))
    return categorical_data_ohe
