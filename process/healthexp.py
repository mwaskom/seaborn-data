import pandas as pd


if __name__ == "__main__":

    G7_countries = {
        "USA": "USA",
        "CAN": "Canada",
        "FRA": "France",
        "DEU": "Germany",
        "ITL": "Italy",
        "GBR": "Great Britain",
        "JPN": "Japan",
        # "CHE": "Switzerland",
        # "DNK": "Denmark",
        # "KOR": "Korea",
        # "BRA": "Brazil",
        # "COL": "Colombia",
        # "CHN": "China",
        # "IND": "India",
    }

    (
        pd.read_csv("raw/healthexp.csv")
        .assign(Country=lambda x: x["Country"].map(G7_countries))
        .dropna(subset=["Country"])
        .to_csv("healthexp.csv", index=False)
    )
