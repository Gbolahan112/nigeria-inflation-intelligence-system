import joblib
import pandas as pd


def load_model():
    model = joblib.load(
        "models/inflation_model.pkl"
    )
    return model


def predict_inflation(
    pump_price,
    cpi_food,
    cpi_energy,
    cpi_transport
):

    model = load_model()

    # --------------------------------
    # Economic Pressure Score
    # --------------------------------
    economic_pressure_score = (
    0.25 * pump_price +
    0.35 * cpi_food +
    0.25 * cpi_transport +
    0.15 * cpi_energy
)

    # --------------------------------
    # Model Features
    # --------------------------------
    features = pd.DataFrame({
        "Pump_Price": [pump_price],
        "CPI_Food": [cpi_food],
        "CPI_Energy": [cpi_energy],
        "CPI_Transport": [cpi_transport],
        "Economic_Pressure_Score": [
            economic_pressure_score
        ]
    })

    prediction = model.predict(features)

    return prediction[0]