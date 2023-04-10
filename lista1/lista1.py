import random
import numpy as np
import matplotlib.pyplot as plt

temperatures = []
for day in range(1,31):
    temperature = random.randint(1, 31)
    temperatures.append(temperature)

plt.xlim(1,31)
plt.plot(range(1, 31), temperatures)
plt.title("Temperatures for 30 days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(np.arange(1, 31))
plt.show()
