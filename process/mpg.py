import pandas as pd


if __name__ == "__main__":

    raw_data = "raw/mpg.csv"
    df = pd.read_csv(raw_data, na_values="?")
    origin_map = {1: "usa", 2: "europe", 3: "japan"}
    df["origin"] = df["origin"].map(origin_map)
    df.to_csv("mpg.csv", index=False)
