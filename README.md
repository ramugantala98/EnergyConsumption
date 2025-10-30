## Energy Consumption Prediction System
**1. Project Overview**
This project demonstrates an end-to-end predictive analytics pipeline for forecasting energy consumption using historical data.
The solution integrates data preprocessing, machine-learning model training, model deployment, and real-time inference through a Streamlit web interface.
The project was fully developed in Python, version-controlled with GitHub, and deployed for public access via Streamlit.io — a free deployment platform for interactive data applications.
 
**2. Objective**
To predict the future energy consumption of households or facilities based on past usage trends and environmental variables.
The goal is to assist in demand forecasting, energy optimization, and sustainability planning.
 
**3. System Architecture**
+-----------------------------+
|       Data Source           |
| (Energy_consumption.csv)    |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Data Preparation       |
| (dataprep.py)               |
| - Cleaning & Transformation |
| - Feature Engineering       |
| - Train/Test Split          |
+-------------+---------------+
              |
              v
+-----------------------------+
|     Model Training          |
| (train.py)                  |
| - LightGBM Regressor        |
| - Hyperparameter Tuning     |
| - Model Serialization (.pkl)|
+-------------+---------------+
              |
              v
+-----------------------------+
|   Model Artifact Storage    |
| (artifact.pkl in repo)      |
+-------------+---------------+
              |
              v
+-----------------------------+
|   Prediction Service        |
| (predict.py + app.py)       |
| - User Input via Streamlit  |
| - Model Loading & Inference |
| - Real-time Visualization   |
+-------------+---------------+
              |
              v
+-----------------------------+
|     Deployment Layer        |
| (Dockerfile + Streamlit.io) |
| - Containerized Environment |
| - Public Web Interface      |
+-----------------------------+
 
**4. Key Components**
File	Purpose
Energy_consumption.csv	Raw dataset used for training and evaluation
dataprep.py	Cleans and prepares the data, handles missing values, encodes categorical variables
train.py	Trains the regression model and saves the model as artifact.pkl
predict.py	Loads the model, performs predictions on new input
app.py	Streamlit app for user interaction and visualization
requirements.txt	Python dependencies for reproducibility
Dockerfile	Container setup for deployment
artifact.pkl	Serialized trained model ready for inference
** 
5. Technical Stack**
•	Programming Language: Python
•	Libraries: Pandas, NumPy, scikit-learn, LightGBM, Joblib, Streamlit
•	Deployment: Streamlit.io (Free Hosting)
•	Version Control: GitHub
•	Containerization: Docker
** 
6. Workflow Summary**
1.	Data Ingestion: Load raw data from Energy_consumption.csv.
2.	Preprocessing: Handle missing values, normalize numerical fields, engineer time-based features.
3.	Model Training: Train and tune a LightGBM regression model to predict future consumption values.
4.	Artifact Storage: Save the trained model as artifact.pkl.
5.	Prediction Service: Load the model via predict.py and use it in a Streamlit web app for interactive predictions.
6.	Deployment: Containerize with Docker and deploy using Streamlit.io, accessible publicly through a web URL.
 
**7. Outcome**
The deployed web app allows users to:
•	Upload or input consumption data,
•	View predicted future energy usage,
•	Analyze patterns through interactive charts and summaries.
This demonstrates an end-to-end MLOps-style pipeline — from data to model to deployment — on a lightweight and free infrastructure.
 
**8. GitHub & Deployment Links (Example placeholders)**
•	GitHub Repository: https://github.com/ramugantala98/EnergyConsumption
•	Live Streamlit App: https://energyconsumption-frhagtwpxqskapnsy2guwr.streamlit.app/
<img width="468" height="644" alt="image" src="https://github.com/user-attachments/assets/6673ebbc-41ed-4be2-93eb-cc2a4cf632e6" />
