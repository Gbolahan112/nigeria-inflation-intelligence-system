import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Load datasets
# -----------------------------
inflation = pd.read_csv("data/inflation.csv")
fuel = pd.read_csv("data/fuel_price.csv")


# -----------------------------
# Rename columns
# -----------------------------
fuel.rename(columns={
    "YEAR": "Year",
    "MONTH": "Month"
}, inplace=True)


# -----------------------------
# Remove missing rows
# -----------------------------
fuel.dropna(inplace=True)


# -----------------------------
# Convert month names to numbers
# -----------------------------
month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

fuel["Month"] = fuel["Month"].map(month_mapping)

fuel["Year"] = fuel["Year"].astype(int)


# -----------------------------
# Merge datasets
# -----------------------------
df = pd.merge(
    inflation,
    fuel[["Year", "Month", "Pump_Price"]],
    on=["Year", "Month"],
    how="left"
)


# -----------------------------
# Fill missing values
# -----------------------------
df["Pump_Price"] = df["Pump_Price"].fillna(
    df["Pump_Price"].median()
)


# -----------------------------
# Correlation analysis
# -----------------------------
correlation = df.corr(numeric_only=True)

print(correlation["Inflation_Rate"].sort_values(ascending=False))


# -----------------------------
# Plot Inflation Trend
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Inflation_Rate"])
plt.title("Nigeria Inflation Trend")
plt.xlabel("Time")
plt.ylabel("Inflation Rate")
plt.show()


# -----------------------------
# Fuel Price vs Inflation
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Pump_Price"], df["Inflation_Rate"])
plt.xlabel("Pump Price")
plt.ylabel("Inflation Rate")
plt.title("Fuel Price vs Inflation")
plt.show()