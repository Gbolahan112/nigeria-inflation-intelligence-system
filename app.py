import streamlit as st
from src.predict import predict_inflation
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="Nigeria Fuel Price & Inflation Intelligence System",
    page_icon="📈",
    layout="centered"
)

# --------------------------------
# Header
# --------------------------------
st.title("📈 Nigeria Fuel Price & Inflation Intelligence System")

st.info(
    "AI-powered economic forecasting system for predicting inflation in Nigeria."
)

st.markdown("""
Predict inflation trends using Machine Learning and economic indicators.

### Key Economic Indicators:
- ⛽ Pump Price
- 🍲 Food CPI
- ⚡ Energy CPI
- 🚚 Transport CPI

This system estimates how fuel and consumer prices influence inflation in Nigeria.
""")

st.markdown("---")


# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("ℹ️ About")

st.sidebar.write("""
This ML system predicts inflation trends
using Nigerian economic indicators.

### Use Cases
- Economists
- Researchers
- Policymakers
- Businesses
- Investors
""")

st.sidebar.markdown("---")

st.sidebar.write("""
📊 Economic Insight:

Inflation in Nigeria is highly influenced by:

- Fuel prices
- Food inflation
- Transport cost
- Energy cost
""")


# --------------------------------
# User Inputs
# --------------------------------
st.subheader("📥 Economic Inputs")

pump_price = st.number_input(
    "⛽ Pump Price (₦)",
    min_value=0.0,
    value=950.0
)

cpi_food = st.number_input(
    "🍲 Food CPI",
    min_value=0.0,
    value=40.0
)

cpi_energy = st.number_input(
    "⚡ Energy CPI",
    min_value=0.0,
    value=35.0
)

cpi_transport = st.number_input(
    "🚚 Transport CPI",
    min_value=0.0,
    value=28.0
)


# --------------------------------
# Charts
# --------------------------------
st.markdown("---")
st.subheader("📊 Economic Indicator Dashboard")

data = {
    "Indicator": [
        "Food CPI",
        "Energy CPI",
        "Transport CPI"
    ],
    "Value": [
        cpi_food,
        cpi_energy,
        cpi_transport
    ]
}

chart_df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    chart_df["Indicator"],
    chart_df["Value"]
)

ax.set_title("Economic Indicator Comparison")
ax.set_ylabel("Index Value")

st.pyplot(fig)


# --------------------------------
# Prediction
# --------------------------------
st.markdown("---")

if st.button("Predict Inflation"):

    prediction = predict_inflation(
        pump_price,
        cpi_food,
        cpi_energy,
        cpi_transport
    )

    st.success(
        f"📈 Predicted Inflation Rate: {prediction:.2f}%"
    )

    st.metric(
    "Predicted Inflation Pressure",
    f"{prediction:.2f}%"
)

    st.caption(
        "Prediction generated using Linear Regression Machine Learning model."
    )

    # --------------------------------
    # Inflation Risk Assessment
    # --------------------------------
    st.subheader("📈 Inflation Risk Assessment")

    if prediction < 10:
        st.success("🟢 Stable Inflation Environment")

    elif prediction < 20:
        st.warning("🟡 Moderate Inflation Pressure")

    elif prediction < 30:
        st.warning("🟠 High Inflation Risk")

    else:
        st.error("🔴 Severe Inflation Pressure")

    # --------------------------------
    # Economic Interpretation
    # --------------------------------
    st.subheader("🧠 Economic Interpretation")

    if prediction < 10:
        st.write("""
        Nigeria is experiencing relatively stable inflation conditions.
        Businesses may face moderate pricing pressure.
        """)

    elif prediction < 20:
        st.write("""
        Inflation pressure is increasing.
        Businesses may experience rising operational costs.
        Consumers may begin to feel price increases.
        """)

    elif prediction < 30:
        st.write("""
        High inflation pressure detected.
        Fuel, transport, and food costs may rise significantly.
        Businesses should prepare for pricing adjustments.
        """)

    else:
        st.write("""
        Severe inflation pressure detected.
        Economic instability risk is high.
        Businesses and households may face substantial cost increases.
        """)


# --------------------------------
# Footer
# --------------------------------
st.markdown("---")

st.caption(
    "Built by Gbolahan | Nigeria Inflation Intelligence System 🚀"
)

st.caption(
    "Disclaimer: Predictions are based on historical economic patterns and should be interpreted as economic estimates, not financial or investment advice."
)