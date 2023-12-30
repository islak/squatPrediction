from . import db
from .models import Metric  # Adjust the import path as needed
import numpy as np  # Import NumPy for data manipulation
from sklearn.linear_model import LinearRegression  # Import the machine learning model

def predict_squat_weight(metrics):
# Perform machine learning prediction
# Example: Predict squat weight based on metrics using a simple linear regression model
    # metrics['water'] + metrics['food']+ metrics['sleep']+
    # Define the maximum percentage reduction for each metric
    max_reduction_percentage = 15

    # Calculate the reduction percentages for each metric
    water_reduction = max_reduction_percentage - (metrics['water'] * max_reduction_percentage / 100)
    food_reduction = max_reduction_percentage - (metrics['food'] * max_reduction_percentage / 100)
    sleep_reduction = max_reduction_percentage - (metrics['sleep'] * max_reduction_percentage / 100)

    # Calculate the predicted squat weight using the reduction percentages
    predicted_weight = (
        metrics['max'] *
        (1 - water_reduction / 100) *
        (1 - food_reduction / 100) *
        (1 - sleep_reduction / 100)
    )

    return predicted_weight

def get_metrics_for_user(user_id):
    # Query the database to retrieve metrics for a specific user
    metric = Metric.query.filter_by(user_id=user_id).first()

    if metric:
        # Create a dictionary with metric values
        metrics = {
            'water': metric.water,
            'food': metric.food,
            'sleep': metric.sleep,
            'max': metric.max
        }

        # Print all metric values
        # print("Water Intake:", metrics['water'])
        # print("Food Consumption:", metrics['food'])
        # print("Sleep Duration:", metrics['sleep'])
        # print("1-Rep Max:", metrics['max'])

        # Return the metrics dictionary
        return metrics
    else:
        print("No metrics found for the user.")
        return None
    



