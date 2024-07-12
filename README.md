# Logistic Regression for Titanic Survival Prediction

This repository contains code and files for building a logistic regression model to predict survival on the Titanic. The dataset used (`titanic_train.csv`) includes passenger information such as age, gender, class, and whether they survived the disaster.

## Files

- `titanic_train.csv`: The dataset used for training the model.
- `logistic_regression.ipynb`: Jupyter Notebook containing the Python code for data preprocessing, model training, and evaluation.
- `app1.py`: This is the python model deployed on streamlit which gives output of no. of survivers by filtering conditions.
- `link`: https://logisticregg-3xtv8felhjd2joz4bkdsao.streamlit.app 

## Libraries Used

- `pandas`: Data manipulation and analysis.
- `numpy`: Mathematical functions on arrays.
- `scikit-learn`: Machine learning tools including model building and evaluation.
- `matplotlib`, `seaborn`: Data visualization.

## Model Building Process

1. **Data Preprocessing**:
   - Handling missing values.
   - Encoding categorical variables.
   - Feature scaling.

2. **Model Training**:
   - Splitting data into training and validation sets.
   - Building and fitting the logistic regression model.

3. **Model Evaluation**:
   - Evaluating performance using accuracy, precision, recall, and F1-score.
   - Confusion matrix and ROC curve analysis.

## How to Use

To run the notebook:
1. Clone this repository:
   ```bash
   git clone https://github.com/tadano13/logisticregg
   cd logisticregg
   ```
2. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Open and Run the Jupyter Notebook:
   ```
   jupyter notebook logistic_regression.ipynb
   ```
4. Execute the Notebook Cells:
```
Follow the instructions in the notebook to execute each cell step-by-step. This includes loading the dataset, preprocessing the data, training the logistic regression model, evaluating its performance, and interpreting the results.
```
# Conclusion
This project demonstrates the application of logistic regression for predicting survival on the Titanic based on passenger attributes. Feel free to explore the notebook for detailed implementation and results.


This version condenses the steps into a more streamlined approach, making it easier for users to follow and replicate your project. Adjust the content as necessary to fit your specific project details and preferences.
Credits<br>
This project is developed by Nishant.
