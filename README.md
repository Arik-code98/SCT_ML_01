# SCT_ML_01
# 🏡 House Price Prediction – SCT_ML_01

This project is a simple machine learning model that predicts house sale prices based on features like above-ground living area, number of bedrooms, and full bathrooms. The model uses **Linear Regression** and provides a **Streamlit UI** for interactive predictions.

---

## 🔍 Project Overview

- **Model Type**: Linear Regression
- **Input Features**:
  - `GrLivArea` (Above Ground Living Area in sq ft)
  - `BedroomAbvGr` (Number of Bedrooms Above Ground)
  - `FullBath` (Number of Full Bathrooms)
- **Target Variable**: `SalePrice` (House Sale Price)
- **Interface**: Streamlit web app

---

## 📁 Repository Structure

| File | Description |
|------|-------------|
| `House_Price_Prediction.ipynb` | Jupyter notebook for training and evaluating the regression model |
| `model.pkl` | Pickle file containing the trained regression model |
| `app.py` | Streamlit app for predicting house prices using the trained model |
| `requirements.txt` | List of required Python packages |
| `README.md` | Project documentation (this file) |

---

## 📦 Installation

 **Clone the repository**
   ```bash
   git clone https://github.com/Arik-code98/SCT_ML_02.git
   cd SCT_ML_02

   streamlit run app.py #This runs the model on a localhost server

Link for the hosted Model 
https://sctml01-mtp9lq3onlfd8wkmjsgttw.streamlit.app/