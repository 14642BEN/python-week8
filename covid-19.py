import pandas as pd
import matplotlib.pyplot as plt

# URL of archived daily state-level data (CSV format)
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"




# Load the dataset into a pandas DataFrame
df = pd.read_csv(url)



# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])



# Sort by date
df = df.sort_values(by='date')

# Basic overview
print("Columns:", df.columns.tolist())
print("\nLatest data:\n", df.tail())

# Plotting daily positive cases over time
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['new_cases'], label='Daily Positive Cases', color='red')
plt.title('Daily COVID-19 Positive Cases in the U.S.')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
