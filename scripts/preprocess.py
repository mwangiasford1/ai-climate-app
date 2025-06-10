import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 🔹 Load the dataset
file_path = '../data/API_EN.GHG.CO2.MT.CE.AR5_DS2_en_csv_v2_3349.csv'
df = pd.read_csv(file_path, encoding='utf-8', delimiter=',', skiprows=4, on_bad_lines='skip', engine='python')

# 🔹 Drop unnecessary columns
df = df.loc[:, ~df.columns.str.contains('Unnamed', case=False)]
df.dropna(how='all', inplace=True)

# 🔹 Clean column names
df.columns = df.columns.str.strip()

# 🔹 Select CO₂ emissions data only
years = [str(year) for year in range(1960, 2024)]
df = df[["Country Name", "Country Code"] + years]

# 🔹 Handle missing values (fill with 0)
df.fillna(0, inplace=True)

# 🔹 Normalize emissions data for ML models
scaler = MinMaxScaler()
df[years] = scaler.fit_transform(df[years])

# 🔹 Save cleaned dataset
processed_file = '../output/processed_emissions.csv'
df.to_csv(processed_file, index=False)

print(f"✅ Preprocessing completed! Clean dataset saved at {processed_file}")