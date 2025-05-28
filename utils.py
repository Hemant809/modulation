import numpy as np
import matplotlib.pyplot as plt
import os

def generate_modulation(msg_freq, msg_amp, msg_waveform,
                        carrier_freq, carrier_amp, carrier_waveform,
                        mod_type):
    t = np.linspace(0, 1, 1000)

    if msg_waveform == "sine":
        message = msg_amp * np.sin(2 * np.pi * msg_freq * t)
    else:
        message = msg_amp * np.cos(2 * np.pi * msg_freq * t)

    if carrier_waveform == "sine":
        carrier = carrier_amp * np.sin(2 * np.pi * carrier_freq * t)
    else:
        carrier = carrier_amp * np.cos(2 * np.pi * carrier_freq * t)

    if mod_type == "AM":
        wave = (1 + message) * carrier
    elif mod_type == "FM":
        wave = carrier_amp * np.sin(2 * np.pi * carrier_freq * t + 5 * message)
    elif mod_type == "PM":
        wave = carrier_amp * np.sin(2 * np.pi * carrier_freq * t + message)
    else:
        raise ValueError("Invalid modulation type")

    os.makedirs("static/plots", exist_ok=True)
    filename = f"{mod_type}_wave.png"
    path = f"static/plots/{filename}"

    plt.figure(figsize=(10, 6))
    plt.plot(t, wave)
    plt.title(f"{mod_type} Modulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig(path)
    plt.close()

    return filename
