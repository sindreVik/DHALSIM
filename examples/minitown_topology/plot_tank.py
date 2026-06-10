import pandas as pd
import matplotlib.pyplot as plt

scada = pd.read_csv("output/scada_values.csv", parse_dates=["timestamp"])
ground = pd.read_csv("output/ground_truth.csv", parse_dates=["timestamp"])

plt.figure(figsize=(12, 5))
plt.plot(scada["timestamp"], scada["TANK"], color="red", label="SCADA values")
plt.plot(ground["timestamp"], ground["TANK_LEVEL"], color="blue", label="Ground truth")

plt.xlabel("Timestamp")
plt.ylabel("Water Level")
plt.title("Tank Water Level: SCADA vs Ground Truth")
plt.legend()
plt.tight_layout()
plt.show()
