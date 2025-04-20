import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data = np.loadtxt("ber_results.csv", delimiter=",", skiprows=1)
snr_db = data[:, 0]
ber = data[:, 1]

# Plot
plt.figure(figsize=(8, 5))
plt.semilogy(snr_db, ber, 'o-', label='Simulated BER')
plt.grid(True, which='both')
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR")
plt.legend()
plt.tight_layout()
plt.show()
