import turtle
import math

# Функція для рекурсивного малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    t.forward(branch_length)  # Малюємо основну гілку
    t.left(45)  # Повертаємо ліворуч на 45 градусів
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)  # Малюємо ліву гілку
    t.right(90)  # Повертаємо праворуч на 90 градусів
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)  # Малюємо праву гілку
    t.left(45)  # Повертаємо ліворуч на 45 градусів
    t.backward(branch_length)  # Повертаємося назад

# Головна функція
def main():
    while True:
        try:
            level = int(input("Enter recursion depth: "))  # Отримуємо рівень рекурсії від користувача
            if level < 0:
                print("Рівень рекурсії має бути невід'ємним числом. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")
    
    screen = turtle.Screen()
    screen.bgcolor("white")  # Встановлюємо білий фон
    t = turtle.Turtle()
    t.speed(0)  # Встановлюємо максимальну швидкість малювання
    t.left(90)  # Повертаємо вгору для початкового положення
    t.up()
    t.goto(0, -200)  # Розташовуємо черепашку внизу екрану
    t.down()
    
    draw_pythagoras_tree(t, 100, level)  # Викликаємо функцію для малювання фрактала
    
    screen.mainloop()  # Залишаємо вікно відкритим

# Виконання основної програми
if __name__ == "__main__":
    main()
