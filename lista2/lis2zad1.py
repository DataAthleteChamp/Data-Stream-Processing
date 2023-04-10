import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych ilości opadów dla każdego dnia miesiąca
np.random.seed(123)
rainfall = np.random.randint(0, 10, size=31)

# Przedstawienie danych na wykresie używając 3 typów wykresów na jednym
fig, ax = plt.subplots(figsize=(10, 6))

# Wykres ciągły
ax.plot(rainfall, linewidth=2, label='ciągły')

# Wykres punktowy
ax.scatter(np.arange(31), rainfall, color='red', label='punktowy')

# Wykres blokowy
ax.bar(np.arange(31), rainfall, alpha=0.3, label='blokowy')

# Ustawienie tytułu i osi
ax.set_title('Ilość opadów w marcu')
ax.set_xlabel('Dzień')
ax.set_ylabel('Ilość opadów')
ax.set_xlim([1, 31])

# Ustawienie legendy
ax.legend()

# Pokazanie wykresu
plt.show()


