# AIM: To load a dataset using Python libraries and perform basic data exploration to understand its structure and summary.
# DESCRIPTION: In this experiment, we learn how to import datasets into Python using the pandas library and explore them to gain basic insights.
# Data exploration involves understanding the dataset's shape, column names, data types, and statistical properties.

import pandas as pd
# Loading the dataset (example: students.csv)
data = pd.read_csv("students.csv")
# Display first 5 rows of the dataset
print("First 5 Rows of Dataset:")
print(data.head())
# Display the number of rows and columns
print("\nShape of the Dataset:")
print(data.shape)
# Display column names
print("\nColumn Names:")
print(data.columns)
# Display statistical summary of numerical columns
print("\nStatistical Summary:")
print(data.describe())
# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())
