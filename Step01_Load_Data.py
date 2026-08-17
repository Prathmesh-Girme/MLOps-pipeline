import pandas as pd


def MarvellousRegression(Datapath):

    # Step 1 : Load the data
    Border = "=" * 40

    print(Border)
    print("Step 1 : Load the data from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)

    print(df.head())


def main():
    
    MarvellousRegression("Data/Advertising.csv")


if __name__ == "__main__":
    main()