####### DATA PREPROCESSING #######
import pandas as pd

## MISSING VALUES
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

## ENCODERS
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def one_hot_encoding(df, unknown='error'):
    # return a new dataframe with encoded features
    df_cat = df.copy().select_dtypes(include=["object"])
    ohe = OneHotEncoder(handle_unknown=unknown).fit(df_cat)
    transformed_array = ohe.transform(df_cat).toarray()
    categorical_data_ohe = pd.DataFrame(transformed_array, columns=ohe.get_feature_names(df_cat.columns))
    return categorical_data_ohe


def drop_columns(df, threshold=None):
    # drop columns that have more missing values than a selected threshold
    columns_to_drop = []
    if threshold:
        missing_v_threshold = threshold
    else:
        missing_v_threshold = float(input('Provide maximum \% of missing values threshold to keep a column (float):'))
    for index, value in df.isnull().sum().iteritems():
        missing_percentage = value/len(df)
        if missing_percentage >= missing_v_threshold:
            columns_to_drop.append(index)
    return df.drop(columns=columns_to_drop)
