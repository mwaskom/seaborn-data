import pandas as pd

def main():

    raw_data = "raw/planets.csv"
    df = pd.read_csv(raw_data, index_col="rowid", skiprows=10)

    df.columns = ["method", "number", "orbital_period",
                  "mass", "distance", "year"]

    df.to_csv("planets.csv", index=False)


if __name__ == "__main__":
    main()
