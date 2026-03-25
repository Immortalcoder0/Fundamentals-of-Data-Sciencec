# AIM: To handle missing values and outliers in a dataset using techniques such as imputation and filtering. [cite: 152, 153]
# DESCRIPTION: Missing values can be handled by replacing them with mean, median, or mode (imputation). [cite: 155, 156]
# Outliers can be handled using filtering or capping methods to remove extreme values. [cite: 157]

import pandas as pd [cite: 161]
import numpy as np [cite: 162]
# Creating a sample dataset with missing and outlier values
data = {'Marks': [85, 90, np.nan, 95, 100, 30, 110, np.nan, 88, 92]} [cite: 163, 165]
df = pd.DataFrame(data) [cite: 166]
print("Original Dataset:") [cite: 168]
print(df) [cite: 168]
# Handling Missing Values - Imputation with Mean
mean_value = df['Marks'].mean() [cite: 171]
df['Marks'].fillna(mean_value, inplace=True) [cite: 172]
print("\nAfter Handling Missing Values (Imputed with Mean):") [cite: 173]
print(df) [cite: 173]
# Handling Outliers - Filtering (Assuming valid marks are 0-100)
filtered_df = df[(df['Marks'] >= 0) & (df['Marks'] <= 100)] [cite: 176]
print("\nAfter Removing Outliers:") [cite: 177]
print(filtered_df) [cite: 178]
