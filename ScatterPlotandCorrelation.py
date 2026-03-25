# AIM: To create scatter plots and calculate correlation coefficients to study variable relationships. [cite: 410, 411]
# DESCRIPTION: A Scatter Plot represents the relationship between two numerical variables. [cite: 413]
# The Correlation Coefficient measures the strength and direction of the linear relationship. [cite: 414]

import pandas as pd [cite: 419]
import matplotlib.pyplot as plt [cite: 420]
# Sample dataset
data = {'Hours Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Marks_Scored': [30, 35, 40, 45, 50, 55, 60, 70, 80, 90]} [cite: 422, 423, 424, 425, 426, 427, 428]
df = pd.DataFrame(data) [cite: 431]
# Scatter Plot
plt.figure(figsize=(6,4)) [cite: 434]
plt.scatter(df['Hours Studied'], df['Marks_Scored'], color='tomato') [cite: 435, 436]
plt.title('Scatter Plot: Hours Studied vs Marks Scored') [cite: 437]
plt.xlabel('Hours Studied') [cite: 438]
plt.ylabel('Marks Scored') [cite: 439]
plt.grid(True) [cite: 440]
plt.show() [cite: 441]
# Calculate Correlation Coefficient
corr = df['Hours Studied'].corr(df['Marks_Scored']) [cite: 443]
print("Correlation Coefficient:", corr) [cite: 443]
