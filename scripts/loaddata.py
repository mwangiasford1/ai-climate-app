import pandas as pd
import matplotlib.pyplot as plt

# Define file path
file_path = 'C:/Users/mwang/OneDrive/Desktop/AI/week 2/assignment week 2/data/API_EN.GHG.CO2.MT.CE.AR5_DS2_en_csv_v2_3349.csv'

# Read CSV while skipping metadata rows and handling delimiter issues
df = pd.read_csv(file_path, encoding='utf-8', delimiter=',', skiprows=4, on_bad_lines='skip', engine='python')

# Drop any unnamed columns
df = df.loc[:, ~df.columns.str.contains('Unnamed')]

# Remove fully empty rows
df.dropna(how='all', inplace=True)

# Replace NaN values with 0
df.fillna(0, inplace=True)

# Clean column names
df.columns = df.columns.str.strip()

# Verify 'Country Name' exists and filter for Kenya
if "Country Name" in df.columns:
    kenya_data = df[df["Country Name"] == "Kenya"]
    
    # Drop unnecessary columns only if kenya_data exists
    kenya_data = kenya_data.drop(columns=["Unnamed: 69"], errors='ignore')

    print(kenya_data)
else:
    print("Error: 'Country Name' column not found. Check column names above.")

kenya_data.to_csv("kenya_emissions.csv", index=False)


years = [str(year) for year in range(1960, 2024)]
emissions = kenya_data.iloc[0][years].astype(float)  # Convert values to float

plt.figure(figsize=(10,5))
plt.plot(years, emissions, marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Mt)")
plt.title("Kenya's CO₂ Emissions Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()