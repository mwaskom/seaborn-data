import numpy as np
import pandas as pd
from scipy import stats


def main():

    rs = np.random.RandomState(24)
    n = 20
    t = 10    

    x = np.linspace(0, t, 100)
    s = np.array([stats.gamma.pdf(x, a) for a in [3, 5, 7]])
    d = s[:, np.newaxis, :]

    d = d * np.array([1, -1])[rs.binomial(1, .3, 3)][:, np.newaxis, np.newaxis]
    d = d + rs.normal(0, .15, (3, n))[:, :, np.newaxis]
    d = d + rs.uniform(0, .25, 3)[:, np.newaxis, np.newaxis]
    d *= 10
    d = d.transpose((1, 2, 0))

    p = pd.Panel(d, 
                 items=pd.Series(np.arange(n), name="subject"),
                 major_axis=pd.Series(x, name="timepoint"),
                 minor_axis=pd.Series(["IPS", "AG", "V1"], name="ROI"),
                 )

    df = p.to_frame().stack().reset_index(name="BOLD signal")
    df.to_csv("gammas.csv", index=False)


if __name__ == "__main__":
    main()
