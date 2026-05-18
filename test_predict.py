from src.predict import predict_inflation


prediction = predict_inflation(
    pump_price=950,
    cpi_food=40,
    cpi_energy=35,
    cpi_transport=28,
    cpi_health=30,
    cpi_education=27,
    production=1.8
)

print(f"Predicted Inflation: {prediction:.2f}%")