# Tracker

🛒 Purchase Prediction System (KNN Algorithm)

A Machine Learning web application that predicts whether a customer will purchase a product based on Age and Salary.
The model is built using the K-Nearest Neighbors (KNN) algorithm and deployed using Streamlit.

🚀 Live Demo
🔗 Click here to view the Live App

📌 About the Project

This project uses a K-Nearest Neighbors (KNN) Classifier trained on the Social Network Ads dataset to predict customer purchase behavior.

Users can interact with the application by adjusting Age and Salary values using sliders, and the model will predict whether the customer is likely to make a purchase.

The application is built using Streamlit (Python) and optimized for deployment on Streamlit Cloud.

🧠 Machine Learning Model
* Algorithm: K-Nearest Neighbors (KNN)
* Library: Scikit-Learn
* Number of Neighbors: k = 300
* Target Variable: Purchased (0 = Not Purchased, 1 = Purchased)

🛠️ Tech Stack
* Frontend: Streamlit
* Backend: Python
* Machine Learning: Scikit-Learn, NumPy
* Model Serialization: Joblib
* Deployment: Streamlit Cloud

📂 Project Structure
.
├── app.py                      # Streamlit application
├── train_model.py              # Model training script
├── ans.pkl                     # Trained KNN model
├── requirements.txt            # List of dependencies
└── DATA_SETS/
    └── Social_Network_Ads.csv  # Dataset

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
Make sure Python is installed, then run:
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📊 Input Features
The model takes the following inputs:
* Age (18 – 100)
* Estimated Salary (₹10,000 – ₹2,00,000)

🎯 Output
* PERSON WILL PURCHASE
* PERSON WILL NOT PURCHASE

💾 Model Training Code (Summary)

* Loads the Social Network Ads dataset
* Splits features (Age, Salary) and target (Purchased)

Trains a KNN classifier
* Saves the trained model using Joblib

🤝 Contributing

Feel free to fork this repository and submit pull requests to improve:
Model performance
UI design
Feature scaling
Additional visualizations
