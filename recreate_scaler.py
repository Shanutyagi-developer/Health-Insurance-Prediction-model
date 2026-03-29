import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
# Replace 'insurance.csv' with the actual dataset file name
data = pd.read_csv("insurance.csv")

# Select numerical columns to scale
num_cols = ["age", "bmi", "bloodpressure", "children"]

# Initialize and fit the scaler
scaler = StandardScaler()
scaler.fit(data[num_cols])

# Save the scaler to a file
joblib.dump(scaler, "scaler.pkl")

print("Scaler recreated and saved as scaler.pkl")