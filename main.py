import calculate_x
import pyramid

while True:
    print("\n=== ГОЛОВНЕ МЕНЮ ===")
    print("1. Обчислити X (Завдання 1)")
    print("2. Побудувати піраміду (Завдання 2)")
    print("0. Вийти з програми")
    
    choice = input("Ваш вибір (0-2): ")

    if choice == "1":
        calculate_x.calculate_x()
    elif choice == "2":
        pyramid.draw_pyramid()
    elif choice == "0":
        print("Роботу завершено.")
        break
    else:
        print("Невідома команда! Спробуйте ще раз.")
