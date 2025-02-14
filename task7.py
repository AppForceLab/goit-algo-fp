import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Количество симуляций
num_simulations = 1_000_000

# Имитация бросков двух кубиков
die1 = np.random.randint(1, 7, num_simulations)
die2 = np.random.randint(1, 7, num_simulations)
sums = die1 + die2

# Подсчет частоты каждой суммы
unique, counts = np.unique(sums, return_counts=True)
monte_carlo_probabilities = counts / num_simulations * 100

# Теоретические вероятности из таблицы
theoretical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Создание DataFrame для сравнения
df = pd.DataFrame({
    "Сумма": unique,
    "Метод Монте-Карло (%)": monte_carlo_probabilities,
    "Теоретическая вероятность (%)": [theoretical_probabilities[s] for s in unique]
})

# Вывод таблицы результатов
print(df)

# Построение графика
plt.figure(figsize=(10, 5))
plt.bar(unique - 0.2, monte_carlo_probabilities, width=0.4, label="Метод Монте-Карло")
plt.bar(unique + 0.2, theoretical_probabilities.values(), width=0.4, label="Теоретические значения")
plt.xlabel("Сумма")
plt.ylabel("Вероятность (%)")
plt.title("Сравнение вероятностей сумм для двух кубиков")
plt.xticks(unique)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
