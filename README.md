# Data analysis
- Document here the project: clem_toolbox
- Description: Project Description
- Data Source:
- Type of analysis:

# Exploratory Data Analysis (EDA)

- Functions to quickly visualize new datasets:

```bash
$ numerical_features_viz(df)

 # plot individual distribution of all numerical features in df
    Histogram
    Boxplot
    QQ-Plot
```

```bash
$ correlation_heat_map(df)
 # return triangle correlation heatmap
```


```bash
$
```


# Continus integration
## Github
Every push of `master` branch will execute `.github/workflows/pythonpackages.yml` docker jobs.
## Gitlab
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.
