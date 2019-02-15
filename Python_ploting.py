
# coding: utf-8


import pandas as pd
import os
from matplotlib import pyplot as plt


os.chdir("/Users/Desktop/Python")
df = pd.read_csv("clus_data.csv")
df.info();

df.info()

# plt.plot(df.M1, df.USERB);
# let's add some legend
plt.style.use("fivethirtyeight")
plt.plot(df.JOBTIME, df.USERB, label="USERB", color="Orange");
plt.plot(df.JOBTIME, df.USERC, label="USERC", linestyle=':', marker='s');
# add y-axis label
plt.ylabel("USERB answers")
plt.legend()
plt.show()
# more on styles:
#'fivethirtyeight' - Based on the color scheme of the popular website
#'grayscale' - Great for when you don't have a color printer!
#'seaborn' - Based on another Python visualization library
#'classic' - The default color scheme for Matplotlib


plt.style.use("ggplot")
plt.plot(df.JOBTIME, df.USERC, label="USERC", linestyle=':', marker='s', color="DarkCyan");
plt.legend()
plt.show()


plt.style.use("seaborn")
plt.plot(df.JOBTIME, df.USERC, label="USERC", linestyle=':', marker='s', color="DarkCyan");
plt.legend()
plt.show()

# to see the all options:
print(plt.style.available)


plt.scatter(df.USERB, df.USERC, color="red", alpha=0.1)
plt.show()


plt.bar(df['USERB'], df['worktime'], color="red")
plt.show()


# range sets the minimum and maximum datapoints that we will include in our histogram.
# bins sets the number of points in our histogram.
# Normalizing the histogram so that the sum of the bins adds to 1 with the density(or normed) keyword.

plt.hist(df.JOBTIME, range= (1, 120), bins=20, normed=True)
plt.show()


