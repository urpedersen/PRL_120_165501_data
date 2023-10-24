import pandas as pd
import matplotlib.pyplot as plt

# Plot of crystallization time, top panel of Fig. 4
plt.figure(figsize=(6, 4))
plt.title('Data from top panel of Figure 3 in PRL 120, 165501 (2018)')
df = pd.read_csv('fastest_crystallization.csv')
plt.plot(df['mole_fraction'], df['time'], 'o')
plt.yscale('log')
plt.xlim(0, 0.5)
plt.xlabel('Mole fraction, $\chi_B$')
plt.ylabel(r'Time, $t^*_\text{min}$')
plt.savefig('crystallization_time.png', dpi=300)
plt.show()

# Setup plot of phase diagram, Fig. 3 main panel
plt.figure(figsize=(12, 8))
plt.title('Data from Figure 3 in PRL 120, 165501 (2018)')

# Coexistence points
df = pd.read_csv('coexistence_points.csv')
for lattice in df['lattice'].unique():
    this = df[df['lattice'] == lattice]
    plt.plot(this['mole_fraction'], this['temperature'], 'o-', label=lattice)

# Iso-diffusivity lines
df = pd.read_csv('iso-diffusivity.csv')
for diffusion_coefficient in df['diffusion_coefficient'].unique():
    this = df[df['diffusion_coefficient'] == diffusion_coefficient]
    plt.plot(this['mole_fraction'], this['temperature'], '--', label=f'D = {diffusion_coefficient:.0e}')

# Temperature of fastest crystallization
df = pd.read_csv('fastest_crystallization.csv')
plt.plot(df['mole_fraction'], df['temperature'], 'g+', label='Fastest crystallization')

# Area with fast crystallization
df = pd.read_csv('rapid_crystallization_fcc.csv')
plt.fill_between(df['mole_fraction'], df['temperature'], 0, color='b', alpha=0.2, label='Rapid crystallization (fcc)')
df = pd.read_csv('rapid_crystallization_CsCl.csv')
plt.fill_between(df['mole_fraction'], df['temperature'], 0, color='r', alpha=0.2, label='Rapid crystallization (CsCl)')

# Finalize plot
plt.xlim(0, 0.5)
plt.ylim(0, 1.5)
plt.xlabel('Mole fraction, $\chi_B$')
plt.ylabel('Temperature, $T$')
plt.legend()
plt.savefig('figure_3.png', dpi=300)
plt.show()
