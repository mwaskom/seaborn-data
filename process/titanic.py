import numpy as np
import pandas as pd

def main():

    raw_data = "raw/titanic.csv"
    df = pd.read_csv(raw_data)

    df["class"] = df.pclass.map({1: "First", 2: "Second", 3: "Third"})
    df["who"] = df[["age", "sex"]].apply(woman_child_or_man, axis=1)
    df["adult_male"] = df.who == "man"
    df["deck"] = df.cabin.str[0].map(lambda s: np.nan if s == "T" else s)
    df["embark_town"] = df.embarked.map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
    df["alive"] = df.survived.map({0: "no", 1: "yes"})
    df["alone"] = ~(df.parch + df.sibsp).astype(bool)
    df = df.drop(["name", "ticket", "cabin"], axis=1)

    df.to_csv("titanic.csv", index=False)


def woman_child_or_man(passenger):
    age, sex = passenger
    if age < 16:
        return "child"
    else:
        return dict(male="man", female="woman")[sex]


if __name__ == "__main__":
    main()
