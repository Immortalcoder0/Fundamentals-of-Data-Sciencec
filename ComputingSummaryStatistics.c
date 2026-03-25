# AIM: To compute summary statistics such as mean, median, mode, and standard deviation for a sample dataset. [cite: 112, 113]
# DESCRIPTION: Statistical measures help describe key characteristics. Mean is the average, Median is the middle value, [cite: 115, 116, 117]
# Mode is the most frequent value, and Standard Deviation measures deviation from the mean. [cite: 118, 119]

import pandas as pd [cite: 123]
from statistics import mean, median, mode, stdev [cite: 124]
# Sample dataset
data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90] [cite: 127]
# Compute summary statistics
mean_val = mean(data) [cite: 128]
median_val = median(data) [cite: 129]
mode_val = mode(data) [cite: 130]
std_dev = stdev(data) [cite: 130]
# Display results
print("Sample Data:", data) [cite: 132]
print("Mean:", mean_val) [cite: 132]
print("Median:", median_val) [cite: 133]
print("Mode:", mode_val) [cite: 134]
print("Standard Deviation:", std_dev) [cite: 135]
