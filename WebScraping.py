# AIM: To perform web scraping on an HTML page using BeautifulSoup and extract table data into a DataFrame. [cite: 289, 290]
# DESCRIPTION: Web scraping is the automatic extraction of data from web pages. [cite: 292]
# BeautifulSoup allows parsing HTML documents to extract specific info like tables and lists. [cite: 293]

import requests [cite: 297]
from bs4 import BeautifulSoup [cite: 298]
import pandas as pd [cite: 299]
# Sample HTML content
html_data = "<table><tr><th>Name</th><th>Age</th><th>Marks</th></tr><tr><td>Ram</td><td>20</td><td>85</td></tr><tr><td>Sita</td><td>19</td><td>90</td></tr><tr><td>Ravi</td><td>21</td><td>78</td></tr></table>" [cite: 300, 301, 302, 303, 304, 306]
# Parse the HTML data
soup = BeautifulSoup(html_data, 'html.parser') [cite: 310, 311]
# Extract table rows
rows = [] [cite: 313]
for tr in soup.find_all('tr'): [cite: 314]
    cols = [td.text for td in tr.find_all(['td', 'th'])] [cite: 315]
    rows.append(cols) [cite: 315]
# Convert to DataFrame
df = pd.DataFrame(rows[1:], columns=rows[0]) [cite: 317]
# Display the DataFrame
print("Extracted DataFrame from HTML Table:") [cite: 319]
print(df) [cite: 319]
