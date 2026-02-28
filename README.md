# Predict Health Insurance Costs

This project predicts health insurance costs based on various factors such as age, BMI, number of children, smoking habits, and region. The project uses machine learning techniques to analyze the data and make predictions.

## Project Structure

- **app.py**: The main application file for running the project.
- **Health insurance Project.ipynb**: A Jupyter Notebook containing data analysis and model training.
- **insurance.csv**: The dataset used for training and testing the model.

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run app.py
   ```

## Dataset

The dataset `insurance.csv` contains the following columns:
- `age`: Age of the individual.
- `sex`: Gender of the individual.
- `bmi`: Body Mass Index.
- `children`: Number of children covered by health insurance.
- `smoker`: Whether the individual is a smoker or not.
- `region`: The region where the individual resides.
- `charges`: The medical charges billed by health insurance.

## Features

- Data preprocessing and visualization.
- Machine learning model for predicting insurance costs.
- Interactive web application using Streamlit.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Scikit-learn
- Joblib

## License

This project is licensed under the MIT License.