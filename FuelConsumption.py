import pandas as pd
import matplotlib.pyplot as plt

# Making data frame
df = pd.read_csv("FuelConsumption.csv")
df.head()

# Plotting the graph for Engine Size vs Co2Emissions
plt.figure(figsize=(7,5))
plt.scatter(df["ENGINESIZE"], df["CO2EMISSIONS"],color="blue")
plt.xlabel("ENGINESIZE")
plt.ylabel("CO2EMISSIONS")
plt.title("Data Plot for Engine Size")
plt.grid()
plt.show()

# Plotting the graph for Cylinders vs Co2Emissions
plt.figure(figsize=(7,5))
plt.scatter(df["CYLINDERS"], df["CO2EMISSIONS"],color="red")
plt.xlabel("CYLINDERS")
plt.ylabel("CO2EMISSIONS")
plt.title("Data Plot for Cylinders")
plt.grid()
plt.show()

# Comnbining Above 2 figures to show Engine Size and Cylinders vs Co2Emissions
plt.figure(figsize=(7,5))
plt.scatter(df["ENGINESIZE"], df["CO2EMISSIONS"],color="blue")
plt.scatter(df["CYLINDERS"], df["CO2EMISSIONS"],color="green")
plt.xlabel("ENGINESIZE and Cylinders")
plt.ylabel("CO2EMISSIONS")
plt.title("Data Plot for Engine Size and Cylinders VS CO2 Emissions")
plt.grid()
plt.show()
