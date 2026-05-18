import joblib
import pandas as pd


def load_model():
    model = joblib.load("models/inflation_model.pkl")
    return model


def predict_inflation(
    pump_price,
    cpi_food,
    cpi_energy,
    cpi_transport,
    cpi_health,
    cpi_education,
    production
):

    model = load_model()

    features = pd.DataFrame({
        "Pump_Price": [pump_price],
        "CPI_Food": [cpi_food],
        "CPI_Energy": [cpi_energy],
        "CPI_Transport": [cpi_transport],
        "CPI_Health": [cpi_health],
        "CPI_Education": [cpi_education],
        "Production": [production]
    })

    prediction = model.predict(features)

    return prediction[0]