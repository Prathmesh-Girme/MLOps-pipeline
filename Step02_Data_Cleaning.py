import pandas as pd


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


def main():
    MarvellousRegression("Data/Advertising.csv")


if __name__ == "__main__":
    main()