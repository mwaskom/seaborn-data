import pandas as pd

if __name__ == "__main__":

    (
        pd.read_csv("raw/seaice.csv")
        .assign(Month=lambda x: x["Month"].ffill())
        .melt(["Month", "Day"], var_name="Year", value_name="Extent")
        .query("1980 <= Year.astype('int') < 2020")
        .astype({"Day": str})
        .dropna()
        .assign(Date=lambda x: pd.to_datetime(
            x[["Day", "Month", "Year"]].apply(" ".join, axis=1)
        ))
        .loc[:, ["Date", "Extent"]]
        .to_csv("seaice.csv", index=False)
    )
