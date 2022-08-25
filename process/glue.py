import pandas as pd

if __name__ == "__main__":

    (
        pd.read_csv("raw/glue.csv")
        .drop(["AX", "MNLI-mm", "WNLI"], axis=1)
        .melt(["Model", "Year", "Encoder"], var_name="Task", value_name="Score")
        .to_csv("glue.csv", index=False)
    )
