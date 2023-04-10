import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych ilości opadów dla każdego dnia miesiąca
rainfall = np.random.randint(0, 10, size=31)

# Ustawienia rozmiarów i marginesów
fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_position([0.1, 0.1, 0.4, 0.8])
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_position([0.6, 0.6, 0.3, 0.3])
ax3 = fig.add_subplot(2, 1, 1)
ax3.set_position([0.6, 0.1, 0.3, 0.3])

# Wykres ciągły (pionowy)
ax1.plot(np.arange(1, 32), rainfall, linewidth=2, label='ciągły')
ax1.set_xlabel('Dzień')
ax1.set_ylabel('Ilość opadów')
ax1.set_xlim([1, 31])
ax1.legend()

# Wykres punktowy (poziomy)
ax2.scatter(np.arange(1, 32), rainfall, color='red', label='punktowy')
ax2.set_xlabel('Dzień')
ax2.set_ylabel('Ilość opadów')
ax2.set_xlim([1, 31])
ax2.legend()

# Wykres blokowy (poziomy)
ax3.bar(np.arange(1, 32), rainfall, alpha=0.3, label='blokowy')
ax3.set_xlabel('Dzień')
ax3.set_ylabel('Ilość opadów')
ax3.set_xlim([1, 31])
ax3.legend()

# Pokazanie wykresów
plt.show()
