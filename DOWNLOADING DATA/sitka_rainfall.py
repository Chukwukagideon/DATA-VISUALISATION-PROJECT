import csv
from datetime import datetime
from shutil import which

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, rainfalls = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        # Add a try except block to handle error in missing values or wrong data type
        try:
            rainfall = row[3]
        except ValueError:
            print(f"Missing data value for {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

# Plotting the values
plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c="blue")

# format the plot
plt.title("Sitka Daily rainfall - 2018", fontsize=24)
plt.xlabel("Date", fontsize=16)
ax.yaxis.set_major_locator(MultipleLocator(5))  # Set major ticks every 5 units
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()