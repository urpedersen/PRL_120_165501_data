import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Predictions from isomorph theory
def isomorph_theory(mole_fraction, density):
    refs = pd.read_csv("liquid.csv")  # Reference state-points at p = 10.19
    # Select reference state-point with same mole fraction
    ref = refs[refs["mole_fraction"] == mole_fraction]
    rho_0 = ref["density"].values[0]
    T_0 = ref["temperature"].values[0]
    gamma = ref["scaling_exponent"].values[0]
    w_0 = ref["virial"].values[0]
    u_0 = ref["energy"].values[0]
    rr0 = density / rho_0
    temperature = T_0 * ((gamma / 2 - 1) * rr0**4 - (gamma / 2 - 2) * rr0**2)
    pressure = density * (
        temperature + (2 * w_0 - 4 * u_0) * rr0**4 + (4 * u_0 - w_0) * rr0**2
    )
    return temperature, pressure


allowed_mole_fractions = pd.read_csv("liquid.csv")["mole_fraction"].unique()
print("Allowed mole fractions:", allowed_mole_fractions)


plt.figure(figsize=(12, 8))
this_python_file = __file__.split("/")[-1]
plt.title(f"Predictions from isomorph theory ({this_python_file})")
for mole_fraction in 0.0, 0.2, 0.319, 0.5:
    densities = np.arange(0.1, 1.8, 0.01)
    temperatures, pressures = isomorph_theory(mole_fraction, densities)
    color = plt.gca()._get_lines.get_next_color()
    plt.plot(
        temperatures,
        pressures,
        "-",
        color=color,
        label=r"$\chi_B$=" f"{mole_fraction} (theory)",
    )
    # Plot true coexistence points
    df = pd.read_csv("isobars.csv")
    this = df[df["mole_fraction"] == mole_fraction]
    plt.plot(
        this["temperature"],
        this["pressure"],
        "o",
        color=color,
        label=r"$\chi_B$=" f"{mole_fraction} (data)",
    )

plt.xlim(0, 3)
plt.ylim(-1, 40)
plt.grid()
plt.xlabel("Temperature, $T$")
plt.ylabel("Pressure, $p$")
plt.legend()
plt.show()
