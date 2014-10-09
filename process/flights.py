import numpy as np
import pandas as pd

def main():

    flights = pd.read_csv("/Users/mwaskom/Desktop/AirPassengers.csv")
    flights["year"] = np.floor(flights.time).astype(int)
    flights["month"] = np.round((flights.time - flights.year) * 12).astype(int)

    month_number_to_name = {0: "January",
                            1: "February",
                            2: "March",
                            3: "April",
                            4: "May",
                            5: "June",
                            6: "July",
                            7: "August",
                            8: "September",
                            9: "October",
                            10: "November",
                            11: "December"}

    flights["month"] = flights.month.map(month_number_to_name)
    flights["passengers"] = flights["AirPassengers"]
    flights = flights.drop(["AirPassengers", "time", "Unnamed: 0"], axis=1)
    flights.to_csv("flights.csv", index=False)


if __name__ == "__main__":
    main()
