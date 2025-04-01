import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        # Handle any errors taht arise from missing data
        try:
            rainfall = row[3]
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

# plot the values
plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c="red")

# format the plot
plt.title("Death Valley daily rainfalls - 2018", fontsize=24)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=15)
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()