import pandas as pd

def main():

    df = pd.read_csv("raw/attention.csv")
    df = pd.melt(df, ["subidr", "attnr"], var_name="solutions", value_name="score")
    df.solutions = df.solutions.str[-1].astype(int)
    df.columns = ["subject", "attention", "solutions", "score"]
    df.to_csv("attention.csv")


if __name__ == "__main__":
    main()
