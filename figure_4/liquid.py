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
    plt.xlabel(r"Mole fraction, $\chi_B$")
    plt.ylabel(f"{variable_name} ({filename})")
plt.text(0.6, 0.1, f"{this_python_file}", transform=plt.gca().transAxes, fontsize=24)
plt.savefig("liquid.png", dpi=300)
plt.show()
