import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(date)

        high = int(row[5])
        highs.append(high)

        low = int(row[-1])
        lows.append(low)


# Plot high and low temperatures
plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")

# Format plot
plt.title("Daily High and Low Temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()