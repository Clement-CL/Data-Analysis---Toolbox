# Toolbox
This document contains modules to speed up data visualisation and preprocessing on new projects.

# Exploratory Data Analysis (EDA)

- Functions to quickly visualize new datasets:


```bash
$ missing_value_vis(df, shape='matrix')
  # Representation of the dataset showing missing values, with three options
  Matrix
  Bar
  Correlation heatmap between missing values
```

```bash
$ correlation_heat_map(df)
  # return triangle correlation heatmap of all numerical features in the dataframe.
```

```bash
$ numerical_features_vis(df)
 # plot distribution of each numerical features in the dataframe.
    Histogram
    Boxplot
    QQ-Plot
```

```bash
$ categorical_features_vis(df)
 # plot distribution of each unique value of categorical features in the dataframe.
```

```bash
$ visualise_all_data(df, shape='matrix')
 # plot distribution of each unique value of categorical features in the dataframe.
```

# Preprocessing

- Functions to preprocess data faster:

```bash
$ drop_columns(df, threshold=None)
  # drop columns that have more missing values than a selected threshold
  # if threshold agrument is not specified user is prompted using input()
```

```bash
$ one_hot_encoding(df, unknown='error')
  # return a new dataframe with encoded features
  # encoded features name = original feature name + value
```

# Continus integration
## Github
Every push of `master` branch will execute `.github/workflows/pythonpackages.yml` docker jobs.
## Gitlab
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.
