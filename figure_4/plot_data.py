import matplotlib.pyplot as plt
import pandas as pd

this_python_file = __file__.split("/")[-1]

# Plot liquid properties
filename = "liquid.csv"
df = pd.read_csv("liquid.csv")
df["pressure"] = df["density"] * (df["temperature"] + df["virial"])
plt.figure(figsize=(12, 8))
for index, variable_name in enumerate(
    ("temperature", "density", "pressure", "scaling_exponent")
):
    plt.subplot(2, 2, index + 1)
    plt.plot(df["mole_fraction"], df[variable_name], "o-")
    plt.xlabel("Mole fraction, $\chi_B$")
    plt.ylabel(f"{variable_name} ({filename})")
plt.text(0.6, 0.2, f"{this_python_file}", transform=plt.gca().transAxes, fontsize=16)
plt.savefig("liquid.png", dpi=300)
plt.show()

# Inset of Figure 4
filename = "Tm_Tonset.csv"
df = pd.read_csv("Tm_Tonset.csv")
plt.figure(figsize=(10, 6))
plt.title(f"Inset of Figure 4 in PRL 120, 165501 (2018); {this_python_file}")
# Plot isobars
for type in df["particle_type"].unique():
    this = df[df["particle_type"] == type]
    plt.plot(
        this["melting_temperature"],
        this["onset_temperature"],
        "o",
        label=f"{type} particles",
    )
plt.xlabel("Melting temperature, $T_m$" f" ({filename})")
plt.ylabel("Onset temperature, $T_0$" f" ({filename})")
plt.text(0.6, 0.2, "$\chi_B=20$%", transform=plt.gca().transAxes, fontsize=16)
plt.legend()
plt.grid()
plt.savefig("Figure_4_inset.png", dpi=300)
plt.show()


# Main panel of Figure 4
filename = "isobars.csv"
df = pd.read_csv(filename)
plt.figure(figsize=(12, 8))
plt.title(f"Main panel of Figure 4 in PRL 120, 165501 (2018); {this_python_file}")
for lattice in df["lattice"].unique():
    this_lattice = df[df["lattice"] == lattice]
    for pressure in this_lattice["pressure"].unique():
        this = this_lattice[this_lattice["pressure"] == pressure]
        plt.plot(
            this["mole_fraction"],
            this["temperature"],
            "o-",
            label=f"{lattice}: $p=${pressure} ({filename})",
        )
filename = "isochor.csv"
df = pd.read_csv(filename)
plt.plot(
    df["mole_fraction"],
    df["temperature"],
    "ko-",
    label=r"FCC: $\rho=1.2$" f"({filename})",
)
plt.xlabel("Mole fraction, $\chi_B$")
plt.ylabel("Temperature, $T$")
plt.legend()
plt.savefig("Figure_4_main_panel.png", dpi=300)
plt.show()
