import pandas as pd

if __name__ == "__main__":

    (
        pd.read_csv("raw/dowjones.csv")
        .set_axis(["Date", "Price"], axis=1)
        .to_csv("dowjones.csv", index=False)
    )
