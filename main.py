import pandas as pd
import matplotlib.pyplot as plt

file_name = "data.csv"

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"error file {file_name} not found")
    exit()
except pd.errors.EmptyDataError:
    print("error file is empty")
    exit()
except pd.errors.ParserError:
    print("error parser error")
    exit()


df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

street_columns = df.columns[1:-2]
print("Available streets:")
for street in street_columns:
    print(street)


selected_street = input("Enter street: ").strip()

if selected_street not in df.columns:
    print(f"Error column {selected_street} not found")
    exit()

df["Total_Cyclists"] = df[selected_street]
monthly_totals = df.groupby("Month")["Total_Cyclists"].sum()
most_popular_month = monthly_totals.idxmax()
max_cyclists = monthly_totals.max()


month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

most_popular_month_name = month_names[most_popular_month]
print(f"The most popular month: {most_popular_month_name}")
print(f"Number of cyclists in this month: {max_cyclists}")


plt.figure(figsize = (15, 8))
daily_totals_street = df.set_index("Date")[selected_street]
plt.plot(daily_totals_street.index, daily_totals_street.values, label = selected_street)

plt.title(f"The number of cyclists for {selected_street} in 2013")
plt.xlabel("Date")
plt.ylabel("The number of cyclists")
plt.legend(loc = "upper left")
plt.grid(True)
plt.tight_layout()
plt.show()