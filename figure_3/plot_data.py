import pandas as pd
import matplotlib.pyplot as plt

this_python_file = __file__.split("/")[-1]

# Plot of crystallization time, top panel of Fig. 4
plt.figure(figsize=(8, 4))
plt.title(f"Top panel of Figure 3 in PRL 120, 165501 (2018); {this_python_file}")
filename = "fastest_crystallization.csv"
df = pd.read_csv(filename)
plt.plot(df["mole_fraction"], df["time"], "o")
plt.yscale("log")
plt.xlim(0, 0.5)
plt.xlabel("Mole fraction, $\chi_B$")
plt.ylabel(r"Time, $t^*_\text{min}$" f"  ({filename})")
plt.grid()
plt.savefig("crystallization_time.png", dpi=300)
plt.show()

# Setup plot of phase diagram, Fig. 3 main panel
plt.figure(figsize=(12, 8))
plt.title("Data from Figure 3 in PRL 120, 165501 (2018); " f"{this_python_file}")

# Coexistence points
filename = "coexistence_points.csv"
df = pd.read_csv(filename)
for lattice in df["lattice"].unique():
    this = df[df["lattice"] == lattice]
    plt.plot(
        this["mole_fraction"],
        this["temperature"],
        "o-",
        label=f"{lattice} ({filename})",
    )

# Iso-diffusivity lines
filename = "iso-diffusivity.csv"
df = pd.read_csv(filename)
for diffusion_coefficient in df["diffusion_coefficient"].unique():
    this = df[df["diffusion_coefficient"] == diffusion_coefficient]
    plt.plot(
        this["mole_fraction"],
        this["temperature"],
        "--",
        label=f"D = {diffusion_coefficient:.0e} ({filename})",
    )

# Temperature of fastest crystallization
filename = "fastest_crystallization.csv"
df = pd.read_csv(filename)
plt.plot(df["mole_fraction"], df["temperature"], "g+", label=f"{filename}")

# Area with fast crystallization
filename = "rapid_crystallization_fcc.csv"
df = pd.read_csv(filename)
plt.fill_between(
    df["mole_fraction"],
    df["temperature"],
    0,
    color="b",
    alpha=0.2,
    label=f"{filename}",
)
filename = "rapid_crystallization_CsCl.csv"
df = pd.read_csv(filename)
plt.fill_between(
    df["mole_fraction"],
    df["temperature"],
    0,
    color="r",
    alpha=0.2,
    label=f"{filename}",
)

# Finalize plot
plt.xlim(0, 0.5)
plt.ylim(0, 1.5)
plt.xlabel("Mole fraction, $\chi_B$")
plt.ylabel("Temperature, $T$")
plt.legend(loc="lower right")
plt.grid()
plt.savefig("phase_diagram.png", dpi=300)
plt.show()
