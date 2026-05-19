#  Nigeria Fuel Price & Inflation Intelligence System

An AI-powered Machine Learning system that predicts inflation pressure in Nigeria using key economic indicators such as fuel price, food inflation, energy cost, and transportation cost.

##  Live Demo

 Streamlit App:  
https://nigeria-inflation-intelligence-system-pbyntgq623pfbmm4pymev2.streamlit.app/

##  Problem Statement

Inflation remains one of Nigeria’s biggest economic challenges.

As fuel prices increase, transportation, food logistics, and production costs also rise — leading to inflationary pressure across the economy.

However, understanding the relationship between fuel price and inflation can be difficult.

This project was built to answer the question:

> **How do fuel prices and economic indicators influence inflation in Nigeria?**

Using Machine Learning, this system predicts inflation pressure based on economic conditions.

---

##  Business Problem

Businesses, policymakers, investors, and researchers often struggle to estimate inflation pressure caused by economic shocks.

For example:

- Increase in fuel price 
- Rising transport costs 
- Increasing food inflation 
- Higher energy costs 

These factors affect:

- Consumer spending
- Business operating costs
- Economic planning
- Investment decisions

This system provides an intelligent way to estimate inflation pressure using historical Nigerian economic data.

---

##  Machine Learning Approach

This project uses:

### Model
- Random Forest Regressor

### Feature Engineering
An **Economic Pressure Score** was engineered to better capture inflation dynamics in Nigeria.

The model combines:

- Pump Price
- Food CPI
- Energy CPI
- Transport CPI

to estimate inflation pressure more realistically.

---

##  Features Used

The model predicts inflation using:

| Feature | Description |
|----------|-------------|
| Pump Price | Petrol price in Nigeria |
| Food CPI | Food inflation index |
| Energy CPI | Energy cost index |
| Transport CPI | Transportation inflation index |
| Economic Pressure Score | Weighted inflation indicator |

---

##  Model Performance

### Performance Metrics

- **MAE:** 0.49
- **R² Score:** 0.98

These results indicate strong predictive performance on historical economic data.

---

##  Dashboard Features

The Streamlit dashboard includes:

✅ Inflation prediction system  

<img width="1895" height="1015" alt="home_dashboard png" src="https://github.com/user-attachments/assets/10a746c0-c31b-4e62-a673-d313ac8c24a6" />

✅ Economic risk assessment  

<img width="1280" height="584" alt="risk_assessment png" src="https://github.com/user-attachments/assets/05dd2349-c754-4a5c-85dc-7605822e8885" />

✅ Professional data visualization 

<img width="1259" height="657" alt="economic_chart png" src="https://github.com/user-attachments/assets/8b39825d-b4b8-494d-b1c3-4107228170ef" />

✅ Interactive user inputs  

<img width="1402" height="553" alt="Screenshot 2026-05-19 092754" src="https://github.com/user-attachments/assets/c24e25e3-143d-459e-a2a7-585e0fa61ce8" />

✅ Economic interpretation insights  

<img width="1230" height="357" alt="prediction_result png" src="https://github.com/user-attachments/assets/d46827f1-bd67-4d4b-995b-2f5c53a655b9" />


---

##  Project Structure

```bash
nigeria-inflation-intelligence-system/
│── data/
│   ├── inflation.csv
│   ├── fuel_price.csv
│
│── models/
│   └── inflation_model.pkl
│
│── src/
│   ├── train.py
│   ├── predict.py
│   └── eda.py
│
│── app.py
│── requirements.txt
│── README.md

🛠️ Installation

Clone repository: git clone https://github.com/Gbolahan112/nigeria-inflation-intelligence-system.git

Move into project: cd nigeria-inflation-intelligence-system

Install dependencies: pip install -r requirements.txt

Run app: streamlit run app.py

🌍 Economic Relevance

This project connects Machine Learning + Economics to analyze real-world Nigerian inflation dynamics.

It demonstrates how ML can support:

Economic intelligence
Financial forecasting
Policy analysis
Business decision-making

 Future Improvements

Future versions may include:

Exchange rate impact
Time series forecasting
Food scarcity indicators
Government policy effects
Oil price volatility


⚠️ Disclaimer

Predictions are based on historical economic patterns and should be interpreted as economic estimates, not financial or investment advice.

 Author

Gbolahan

Machine Learning | Data Analytics | Economic Intelligence































