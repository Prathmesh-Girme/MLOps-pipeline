import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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
    
     #step 3 :Check missing value
    
    print(Border)
    print("Step 3 : Check missing value")
    print(Border)
    
    # print(df.isnull().sum())
    
    print(Border)
    
    print("Total missing values : ")
    print(Border)
    print(df.isnull().sum().sum())
    print(Border)
    
    
    
    #step 4 = statistical Summary of data
    
    print(Border)
    print("Step 4 : Statistical Summary of data")
    print(Border)
    
    print(df.describe())
    
    
    #step 5 : correlation between independent and dependent variable
    
    print(Border)
    print("Step 5 : Correlation between independent and dependent variable")
    print(Border)
    
    print(df.corr())
    
    #step 6 : seperate the data into independent and dependent variable
    print(Border)
    print("Step 6 : seperate   the data into independent and dependent variable")
    print(Border)
    
    X = df[['TV', 'radio' , 'newspaper']]  # Example: using 'TV' and 'radio' , "newspaper" as the independent variables 
    Y = df['sales']  # Example: using 'Sales' as the dependent variable
    
    print("Independent variable X : ")
    print(X.head())
    
    print("Dependent variable Y : ")
    print(Y.head())
    
    #step 7 : Split the data into training and testing sets
    print(Border)
    print("Step 7 : Split the data into training and testing sets")
    print(Border)
    
    
    X_train , X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)
    
    #step 8 : Create a Linear Regression model and train it
    
    print(Border)
    print("Step 8 : Create a Linear Regression model and train it")
    print(Border)
    
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    print("model trained successfully...")
    
    
    #step 9 : test the model
    
    print(Border)
    print("step 9 : test the model")
    print(Border)
    
    Y_pred = model.predict(X_test)
    
    
    print("Expected answers")
    print(Y_test[:3])
    
    print("Predicted answers")
    print(Y_pred[:3])
    
    


def main():
    MarvellousRegression("Data/Advertising.csv")


if __name__ == "__main__":
    main()