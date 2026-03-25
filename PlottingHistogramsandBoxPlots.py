# AIM: To plot histograms and box plots to understand the distribution and spread of a single variable. [cite: 342, 343]
# DESCRIPTION: A Histogram shows frequency distribution in intervals (bins) to visualize shape and spread. [cite: 345, 346]
# A Box Plot displays distribution based on five summary stats and identifies outliers. [cite: 348, 349]

import pandas as pd [cite: 352]
import matplotlib.pyplot as plt [cite: 353]
# Sample dataset
data = {'Marks': [55, 60, 65, 70, 72, 74, 78, 80, 82, 85, 88, 90, 92, 95, 98]} [cite: 355, 356, 357]
df = pd.DataFrame(data) [cite: 359]
# Plotting Histogram
plt.figure(figsize=(6,4)) [cite: 361]
plt.hist(df['Marks'], bins=5, color='skyblue', edgecolor='black') [cite: 363]
plt.title('Histogram of Marks') [cite: 364]
plt.xlabel('Marks') [cite: 365]
plt.ylabel('Frequency') [cite: 366]
plt.show() [cite: 367]
# Plotting Box Plot
plt.figure(figsize=(4,5)) [cite: 369]
plt.boxplot(df['Marks'], patch_artist=True, boxprops=dict(facecolor='lightgreen')) [cite: 370, 371]
plt.title('Box Plot of Marks') [cite: 372]
plt.ylabel('Marks') [cite: 373]
plt.show() [cite: 374]
