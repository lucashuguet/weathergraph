#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data from st cere

officielstcere = pd.read_csv("csv/stcere-officiel-2mai7mai.csv", delimiter=";")
raspistcere = pd.read_csv("csv/stcere-raspi-2mai7mai.csv", delimiter=";")

fig, (ax1, ax2) = plt.subplots(2, 1)

offtemp = 0
offhumi = 0
offpres = 0

for i in officielstcere.Temperature:
    offtemp += i
for i in officielstcere.Humidity:
    offhumi += i
for i in officielstcere.Pressure:
    offpres += round(i/10, 3)

rastemp = 0
rashumi = 0
raspres = 0

for i in raspistcere.Temperature:
    rastemp += i
for i in raspistcere.Humidity:
    rashumi += i
for i in raspistcere.Pressure:
    raspres += round(i/10, 3)

# data le blanc

officielleblanc = pd.read_csv("csv/leblanc-officiel-25avril29avril.csv", delimiter=";")
raspileblanc = pd.read_csv("csv/leblanc-raspi-25avril29avril.csv", delimiter=";")

fig, (ax1, ax2) = plt.subplots(2, 1)

for i in officielleblanc.Temperature:
    offtemp += i
offtemp = offtemp/(len(officielleblanc.Temperature) + len(officielstcere.Temperature))

for i in officielleblanc.Humidity:
    offhumi += i
offhumi = offhumi/(len(officielleblanc.Humidity) + len(officielstcere.Humidity))

for i in officielleblanc.Pressure:
    offpres += round(i/10, 3)
offpres = offpres/(len(officielleblanc.Pressure) + len(officielstcere.Pressure))


for i in raspileblanc.Temperature:
    rastemp += i
rastemp = rastemp/(len(raspileblanc.Temperature) + len(raspistcere.Temperature))

for i in raspileblanc.Humidity:
    rashumi += i
rashumi = rashumi/(len(raspileblanc.Humidity) + len(raspistcere.Humidity))

for i in raspileblanc.Pressure:
    raspres += round(i/10, 3)
raspres = raspres/(len(raspileblanc.Pressure) + len(raspistcere.Pressure))


labels = ["Température (en °C)", "Humidité (en %)", "Pression (en x10 Pa)"]
width = 0.35

fig, ax = plt.subplots()
x = np.arange(len(labels))

off = [round(offtemp, 1), round(offhumi, 1), round(offpres, 2)]
ras = [round(rastemp, 1), round(rashumi, 1), round(raspres, 2)]

rects1 = ax.bar(x - width/2, off, width, label='Météo France')
rects2 = ax.bar(x + width/2, ras, width, label='Station Météo Maison')

ax.set_ylabel('Mesures')
ax.set_title('Moyennes sur deux semaines de mesures')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
fig.set_figwidth(16)
fig.set_figheight(9)

plt.savefig("img/histogram.png")
