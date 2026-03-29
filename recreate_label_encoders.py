import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv("insurance.csv")

# Recreate label encoders
le_gender = LabelEncoder()
le_gender.fit(data["gender"])
joblib.dump(le_gender, "label_encoder_gender.pkl")

le_diabetic = LabelEncoder()
le_diabetic.fit(data["diabetic"])
joblib.dump(le_diabetic, "label_encoder_diabetic.pkl")

le_smoker = LabelEncoder()
le_smoker.fit(data["smoker"])
joblib.dump(le_smoker, "label_encoder_smoker.pkl")

print("Label encoders recreated and saved.")