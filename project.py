import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")

del df["Luminosity"]

data = []

with open("bright_stars.csv") as f:
  csvreader = csv.reader(f)

for i in data:
    if(i[0]=="?"):
        data.remove(i)
    if(i[1]=="?"):
        data.remove(i)
    if(i[2]=="?"):
        data.remove(i)
    if(i[3]=="?"):
        data.remove(i)

data.to_csv("main.csv")