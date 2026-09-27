def draw_pyramid():
    print("\nЗавдання 2: Малюнок (Ромб)")
    
    for i in range(1, 11):
        spaces = " " * (10 - i)
        numbers = f"{i} " * i
        print(spaces + numbers.strip())
        

    for i in range(9, 0, -1):
        spaces = " " * (10 - i)
        numbers = f"{i} " * i
        print(spaces + numbers.strip())
