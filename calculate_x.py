def calculate_x():
    try:
        b = float(input("Введіть значення числа b: "))
        a = float(input("Введіть значення числа a: "))
    except ValueError:
        print("Помилка! Вводьте лише числа.")
        return

    if a > b:
        print(b * a + 1)
    elif a == b:
        print(3425)
    elif a < b:
        if b == 0:
            print("Помилка! Ділення на нуль неможливе.")
        else:
            print((2 * a - 5) / b)
          

