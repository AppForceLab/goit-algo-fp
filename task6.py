def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if budget >= info["cost"]:
            selected_items.append(item)
            total_calories += info["calories"]
            budget -= info["cost"]
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    costs = [items[item]["cost"] for item in item_names]
    calories = [items[item]["calories"] for item in item_names]
    
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення обраних предметів
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]
    
    return selected_items, dp[n][budget]


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print("Greedy Algorithm:", greedy_algorithm(items, budget))
print("Dynamic Programming:", dynamic_programming(items, budget))
