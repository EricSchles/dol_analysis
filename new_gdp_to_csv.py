import pandas as pd

with open("gdp_values.txt", "r") as f:
    text = f.read().split("\n")
gdps = pd.DataFrame()
for line in text[1:]:
    line = line.split()
    if line == []:
        continue
    gdps = gdps.append({
        "2016": float(line[0]),
        "2017": float(line[1]),
        "2018": float(line[2]),
        "2019": float(line[3]),
        "2020": float(line[4])
    }, ignore_index=True)
with open("countries.txt", "r") as f:
    countries = f.read().split("\n")
df = gdps.copy()
df["countries"] = countries
df.to_csv("gdp.csv")
