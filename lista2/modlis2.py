import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych ilości opadów dla każdego dnia miesiąca
rainfall = np.random.randint(0, 10, size=31)

# Wykres ciągły (pionowy)
plt.subplot(212)
plt.plot(np.arange(1, 32), rainfall, linewidth=2, label='ciągły')
plt.xlabel('Dzień')
plt.ylabel('Ilość opadów')
plt.xticks(np.arange(1, 32))
plt.legend()

# Wykres punktowy (poziomy)
plt.subplot(221)
plt.scatter(np.arange(1, 32), rainfall, color='red', label='punktowy')
plt.xlabel('Dzień')
plt.ylabel('Ilość opadów')
plt.xticks(np.arange(1, 32))
plt.legend()

# Wykres blokowy (poziomy)
plt.subplot(222)
plt.bar(np.arange(1, 32), rainfall, alpha=0.3, label='blokowy')
plt.xlabel('Dzień')
plt.ylabel('Ilość opadów')
plt.xticks(np.arange(1, 32))
plt.legend()

# Pokazanie wykresów
plt.show()
