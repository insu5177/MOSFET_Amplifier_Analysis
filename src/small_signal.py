import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Parameters
# -----------------------------
Vth = 1.2      # Threshold voltage
k = 0.5        # MOSFET parameter
Rd = 10        # Drain resistor
Vdd = 5        # Supply voltage

Vbias = 1.5    # Bias point

# -----------------------------
# 2. Time & Input Signal
# -----------------------------
t = np.linspace(0, 1, 1000)

# Small signal input
Vin = 0.05 * np.sin(2 * np.pi * 5 * t)

# -----------------------------
# 3. MOSFET Model
# -----------------------------
Vgs = Vbias + Vin
Id = np.where(Vgs > Vth, k * (Vgs - Vth)**2, 0)

# -----------------------------
# 4. Output Voltage
# -----------------------------
Vout = Vdd - Rd * Id

# 🔥 AC 성분만 추출 (핵심)
Vout_ac = Vout - np.mean(Vout)

# -----------------------------
# 5. Plot
# -----------------------------
plt.figure()

plt.plot(t, Vin, label="Vin (Input)")
plt.plot(t, Vout_ac, label="Vout (AC Output)")

plt.title("Small Signal Amplification (AC Component)")
plt.xlabel("Time")
plt.ylabel("Voltage")

plt.legend()
plt.grid()

plt.show()