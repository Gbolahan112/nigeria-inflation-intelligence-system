import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


# -----------------------------
# Load datasets
# -----------------------------
inflation = pd.read_csv("data/inflation.csv")
fuel = pd.read_csv("data/fuel_price.csv")


# -----------------------------
# Clean fuel data
# -----------------------------
fuel.rename(columns={
    "YEAR": "Year",
    "MONTH": "Month"
}, inplace=True)

fuel.dropna(inplace=True)

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

df["Pump_Price"] = df["Pump_Price"].fillna(
    df["Pump_Price"].median()
)


# -----------------------------
# Economic Pressure Score
# -----------------------------
df["Economic_Pressure_Score"] = (
    0.25 * df["Pump_Price"] +
    0.35 * df["CPI_Food"] +
    0.25 * df["CPI_Transport"] +
    0.15 * df["CPI_Energy"]
)


# -----------------------------
# Features & Target
# -----------------------------
X = df[
    [
        "Pump_Price",
        "CPI_Food",
        "CPI_Energy",
        "CPI_Transport",
        "Economic_Pressure_Score"
    ]
]

y = df["Inflation_Rate"]


# -----------------------------
# Remove Missing Values
# -----------------------------
df = df.dropna()


# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# Train Model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)


# -----------------------------
# Predictions
# -----------------------------
predictions = model.predict(X_test)


# -----------------------------
# Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\nMAE: {mae:.4f}")
print(f"R2 Score: {r2:.4f}")


# -----------------------------
# Feature Importance
# -----------------------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(
    importance.sort_values(
        by="Importance",
        ascending=False
    )
)


# -----------------------------
# Save model
# -----------------------------
joblib.dump(
    model,
    "models/inflation_model.pkl"
)

print("\nModel saved successfully!")