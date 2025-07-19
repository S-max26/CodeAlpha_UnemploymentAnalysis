# unemployment_analysis_v2.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
dataset_path = "C:/Users/shash/OneDrive/Desktop/Internship 2/task 2/Unemployment_Rate_upto_11_2020.csv"
unemp_data = pd.read_csv(dataset_path)

# Clean column names and date entries
unemp_data.columns = unemp_data.columns.str.strip()
unemp_data['Date'] = unemp_data['Date'].str.strip()

# Convert 'Date' column to datetime
unemp_data['Date'] = pd.to_datetime(unemp_data['Date'], format="%d-%m-%Y")

# Rename columns for better readability
unemp_data.rename(columns={
    'Region': 'State',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation',
    'Region.1': 'Region'
}, inplace=True)

# Sort dataset chronologically
unemp_data = unemp_data.sort_values(by='Date')

# Display basic dataset information
print("\n📊 Sample Data:\n", unemp_data.head())
print("\n🧾 Dataset Info:\n")
unemp_data.info()
print("\n🔍 Missing Values:\n", unemp_data.isnull().sum())

# ------------------------- Visualization Section -------------------------

# Line plot: Overall unemployment trend in India
plt.figure(figsize=(12, 6))
sns.lineplot(data=unemp_data, x='Date', y='Unemployment_Rate', errorbar=None, color='teal')
plt.title("India's Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Boxplot: State-wise unemployment rate distribution (Top 10 states by data availability)
plt.figure(figsize=(14, 7))
popular_states = unemp_data['State'].value_counts().index[:10]
sns.boxplot(data=unemp_data[unemp_data['State'].isin(popular_states)], 
            x='State', y='Unemployment_Rate', palette='pastel')
plt.xticks(rotation=45)
plt.title("State-wise Unemployment Rate Distribution")
plt.tight_layout()
plt.show()

# Line plot: Unemployment trend during COVID-19 (March 2020 onwards)
covid_period = unemp_data[unemp_data['Date'] >= "2020-03-01"]

plt.figure(figsize=(12, 6))
sns.lineplot(data=covid_period, x='Date', y='Unemployment_Rate', color='coral')
plt.title("Unemployment Rate During COVID-19 (March 2020 onward)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Bar plot: Monthly average unemployment rates
unemp_data['Month'] = unemp_data['Date'].dt.month
monthly_avg_unemp = unemp_data.groupby('Month')['Unemployment_Rate'].mean()

plt.figure(figsize=(10, 5))
monthly_avg_unemp.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Monthly Average Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
