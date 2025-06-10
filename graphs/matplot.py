# import necessary libraries
import matplotlib.pyplot as plt



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