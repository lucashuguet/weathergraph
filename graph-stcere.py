#!/usr/bin/env python3
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

officiel = pd.read_csv("csv/stcere-officiel-2mai7mai.csv", delimiter=";")
raspi = pd.read_csv("csv/stcere-raspi-2mai7mai.csv", delimiter=";")

fig, (ax1, ax2) = plt.subplots(2, 1)

offtemp = []
offhumi = []
offpres = []

for i in officiel.Temperature:
    offtemp.append(i)
for i in officiel.Humidity:
    offhumi.append(i)
for i in officiel.Pressure:
    offpres.append(round(i/10, 2))

rastemp = []
rashumi = []
raspres = []

for i in raspi.Temperature:
    rastemp.append(i)
for i in raspi.Humidity:
    rashumi.append(i)
for i in raspi.Pressure:
    raspres.append(round(i/10, 2))

t = []
it = 2.0

for i in range(len(officiel.Time)):
    t.append(it)
    it += 3.0

major_ticks = np.arange(0, len(officiel.Time) *3, 24)
minor_ticks = np.arange(2, len(officiel.Time) *3, 3)

ax1.plot(t, offtemp, label="Température (en °C)")
ax1.plot(t, offhumi, label="Humidité (en %)")
ax1.plot(t, offpres, label="Pression (en kPa)")
ax1.set_xlabel("Temps (en heures)")
ax1.set_title("Observations de Météo France")
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)
ax1.grid(True)

ax2.plot(t, rastemp, label="Température (en °C)")
ax2.plot(t, rashumi, label="Humidité (en %)")
ax2.plot(t, raspres, label="Pression (en kPa)")
ax2.set_xlabel("Temps (en heures)")
ax2.set_title("Mesures de notre Station Météo")
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.grid(True)

fig.tight_layout()
fig.legend(["Température (en °C)", "Humidité (en %)", "Pression (en kPa)"])
fig.set_figwidth(16)
fig.set_figheight(9)
fig.suptitle("Observations météorologiques de Saint Céré, du 2 au 7 mai 2022", fontsize="xx-large")

plt.savefig("img/stcere.svg")
