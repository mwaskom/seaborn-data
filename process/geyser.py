import numpy as np
import pandas as pd
from scipy.cluster.vq import kmeans2

if __name__ == "__main__":

    np.random.seed(0)

    df = pd.read_csv("raw/geyser.csv")
    df.columns = ["duration", "waiting"]

    _, z = kmeans2(df, 2)
    df["kind"] = np.where(z, "long", "short")

    df.to_csv("geyser.csv", index=False)
