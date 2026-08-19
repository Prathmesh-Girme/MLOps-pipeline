import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def MarvellousRegression(Datapath):

    Border = "=" * 40

    # Step 1 : Load the data
    print(Border)
    print("Step 1 : Load the data from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)

    print(df.head())

    # Step 2 : Remove unwanted columns
    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    print(df.head())

    # Step 3 : Check missing values
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Total missing values :")
    print(df.isnull().sum().sum())

    print(Border)

    # Step 4 : Statistical Summary of data
    print(Border)
    print("Step 4 : Statistical Summary of data")
    print(Border)

    print(df.describe())

    # Step 5 : Correlation between independent and dependent variables
    print(Border)
    print("Step 5 : Correlation between independent and dependent variables")
    print(Border)

    print(df.corr())

    # Step 6 : Separate data into independent and dependent variables
    print(Border)
    print("Step 6 : Separate data into independent and dependent variables")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent variable X :")
    print(X.head())

    print("Dependent variable Y :")
    print(Y.head())

    # Step 7 : Split the data into training and testing sets
    print(Border)
    print("Step 7 : Split the data into training and testing sets")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

    # Step 8 : Create a Linear Regression model and train it
    print(Border)
    print("Step 8 : Create a Linear Regression model and train it")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    print("Model trained successfully...")

    # Step 9 : Test the model
    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Expected answers :")
    print(Y_test[:3])

    print("Predicted answers :")
    print(Y_pred[:3])

    # Step 10 : Evaluate the model
    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("Mean Squared Error :", MSE)
    print("Root Mean Squared Error :", RMSE)
    print("R2 Score :", R2)

    # Step 11 : Display coefficients of the model
    print(Border)
    print("Step 11 : Display coefficients of the model")
    print(Border)

    print("TV Coefficient :", model.coef_[0])
    print("Radio Coefficient :", model.coef_[1])
    print("Newspaper Coefficient :", model.coef_[2])

    print("Intercept :", model.intercept_)

    print(Border)
    print("Linear Regression Pipeline Completed Successfully")
    print(Border)


def main():

    MarvellousRegression("Data/Advertising.csv")


if __name__ == "__main__":
    main()