import pandas as pd
import numpy as np

####### DATA VISUALIZATION #######
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import missingno as mn


def missing_value_viz(df, shape='matrix'):
    # return a bar representation of missing values and correlation between missing values
    if shape=='all':
        mn.matrix(df, color=(142/255, 187/255, 217/255))
        mn.heatmap(df)
    if shape=='matrix':
        mn.matrix(df, color=(142/255, 187/255, 217/255))
    if shape=='heatmap':
        mn.heatmap(df)

def numerical_features_viz(df):
  num_data = df._get_numeric_data()
  for feature in num_data.columns:
      fig, ((ax0, ax1, ax2)) = plt.subplots(1,3,figsize=(20,6))
      sns.histplot(data=num_data, x=feature, kde=True, ax=ax0).set_title(f'{feature}_Distribution')
      sns.boxplot(data=num_data, x=feature, ax=ax1).set_title(f'{feature}_Boxplot')
      ax2=sm.qqplot(num_data[feature],line='s',ax=ax2)


def correlation_heat_map(df):
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


def vizualise_data(df, shape='matrix'):
    missing_value_viz(df, shape=shape)
    numerical_features_viz(df)
    correlation_heat_map(df)




