import pandas as pd

COLUMN_MAP = {
    "tpep_pickup_datetime": "pickup",
    "tpep_dropoff_datetime": "dropoff",
    "passenger_count": "passengers",
    "trip_distance": "distance",
    "fare_amount": "fare",
    "tip_amount": "tip",
    "tolls_amount": "tolls",
    "total_amount": "total",
    "color": "color",
}

PAYMENT_TYPES = {
    1: "credit card",
    2: "cash",
}

MAX_TRIP_DURATION = 8000

if __name__ == "__main__":

    raw = pd.read_csv(
        "raw/taxis.csv",
        parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"]
    ).rename(columns=str.lower)

    loc = pd.read_csv("raw/taxi_zones.csv").set_index("LocationID").drop_duplicates()

    clean = (
        raw[list(COLUMN_MAP)]
        .rename(columns=COLUMN_MAP)
        .assign(payment=raw["payment_type"].map(PAYMENT_TYPES))
        .assign(pickup_zone=raw["pulocationid"].map(loc["zone"]))
        .assign(dropoff_zone=raw["dolocationid"].map(loc["zone"]))
        .assign(pickup_borough=raw["pulocationid"].map(loc["borough"]))
        .assign(dropoff_borough=raw["dolocationid"].map(loc["borough"]))
        .loc[lambda x: x["dropoff_borough"] != "EWR"]
        .loc[lambda x: x.eval("dropoff - pickup").dt.seconds < MAX_TRIP_DURATION]
        .loc[lambda x: (x["fare"] > 0) & (x["fare"] < 200)]
        .loc[lambda x: (x["tip"] / x["fare"]) < 1]
    )

    clean.to_csv("taxis.csv", index=False)