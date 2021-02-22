import pandas as pd
import numpy as np

####### DATA VISUALIZATION #######
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import missingno as mn


def missing_value_vis(df, shape='matrix'):
    # return a bar representation of missing values and correlation between missing values
    is_NaN = df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    print(f'''
      \n \033[1m\033[4mDataset missing values:\033[0m
      \n
      * {len(df[row_has_NaN])} ({round(len(df[row_has_NaN])/len(df)*100,2)}% of total) rows have at least one missing value.
      \n
      ''')

    if shape=='all':
        mn.matrix(df, color=(142/255, 187/255, 217/255))
        mn.heatmap(df)
    if shape=='matrix':
        mn.matrix(df, color=(142/255, 187/255, 217/255))
    if shape=='heatmap':
        mn.heatmap(df)

def correlation_heat_map(df):
    assert type(df) == pandas.core.frame.DataFrame
    print('''
      \n \033[1m\033[4mFeature correlation:\033[0m\n
      ''')
    corrs = df.corr()
    # Set the default matplotlib figure size:
    fig, ax = plt.subplots(figsize=(12, 12))
    # Generate a mask for the upper triangle (taken from seaborn example gallery)
    mask = np.zeros_like(corrs, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    # Plot the heatmap with seaborn.
    # Assign the matplotlib axis the function returns. This will let us resize the labels.
    ax = sns.heatmap(corrs, mask=mask, annot=True, cmap='coolwarm')
    # Resize the labels.
    ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14, rotation=30)
    ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14, rotation=0)
    # If you put plt.show() at the bottom, it prevents those useless printouts from matplotlib.
    plt.show()

def numerical_features_vis(df):
    # Return an histogram, a boxplot and a qqplot for all numerical columns
    print('''
      \n \033[1m\033[4mNumerical features distribution:\033[0m \n
      ''')
    num_data = df._get_numeric_data()
    for feature in num_data.columns:
        print(f'\033[4m{feature.capitalize()}\033[0m')
        fig, ((ax0, ax1, ax2)) = plt.subplots(1,3,figsize=(20,4))
        sns.histplot(data=num_data, x=feature, kde=True, ax=ax0).set_title(f'{feature}_Distribution')
        sns.boxplot(data=num_data, x=feature, ax=ax1).set_title(f'{feature}_Boxplot')
        ax2=sm.qqplot(num_data[feature],line='s',ax=ax2, color=(120/255, 157/255, 200/255))
        plt.show()

def categorical_features_vis(df):
    # Return a bar chart showing the repartition between unique values
    print('''
      \n \033[1m\033[4mCategorical features distribution:\033[0m \n
      ''')
    cat_data = df.copy().fillna('MISSING').select_dtypes(include=["object"])
    for feature in cat_data:
        print(f'\033[4m{feature.capitalize()}\033[0m')
        pd.value_counts(cat_data[feature]).plot.bar(figsize=(12,4), color=(142/255, 187/255, 217/255), edgecolor='black')
        plt.show()


def visualise_all_data(df, shape='matrix'):
    missing_value_vis(df, shape=shape)
    plt.show()
    correlation_heat_map(df)
    plt.show()
    numerical_features_vis(df)
    plt.show()
    categorical_features_vis(df)
    plt.show()

