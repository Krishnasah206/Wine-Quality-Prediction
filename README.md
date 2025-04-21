# 🍷 Wine Quality Prediction Web App

This is a machine learning web app built using **K-Nearest Neighbors (KNN)** algorithm to predict the quality of wine based on various chemical features. The web app is developed with **Streamlit** and deployed on **Streamlit Community Cloud**.

---

## 📊 Dataset

-> https://www.kaggle.com/datasets/yasserh/wine-quality-dataset

The dataset used for this project includes the following features:

- fixed acidity  
- volatile acidity  
- citric acid  
- residual sugar  
- chlorides  
- free sulfur dioxide  
- total sulfur dioxide  
- density  
- pH  
- sulphates  
- alcohol  
- quality (target variable)  
- Id (removed during preprocessing)

---

## 🧠 Model

The machine learning model is built using the **K-Nearest Neighbors (KNN)** algorithm with the following steps:

1. Load the wine quality dataset.
2. Drop the `Id` column.
3. Split the data into training and test sets.
4. Standardize the feature values using `StandardScaler`.
5. Train the KNN model.
6. Evaluate and save the model and scaler using `joblib`.

---

## 💻 Streamlit Web App

The Streamlit app (`app.py`) allows users to input wine features through sliders and number inputs, then predicts the wine quality based on the trained KNN model.

---

## 🚀 Deployment

The app is deployed using **Streamlit Community Cloud**.

### 🔗 [Live Demo](https://krishnasah206-wine-quality-prediction-app-hhxmro.streamlit.app/) -> https://krishnasah206-wine-quality-prediction-app-hhxmro.streamlit.app/

---

## 🗂 Project Structure

```
wine-quality-knn-app/
│
├── wineQT.csv              # Dataset
├── wine_quality_knn.ipynb     # Jupyter Notebook for training
├── app.py                     # Streamlit web app
├── knn_model.pkl              # Trained KNN model
├── scaler.pkl                 # Scaler used in preprocessing
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Krishnasah206/Wine-Quality-Prediction
   cd Wine-Quality-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy, scikit-learn
- Streamlit
- Joblib

---

## ✍️ Author

**Krishna Kumar Sah**  
Feel free to connect with me for any queries or collaboration.