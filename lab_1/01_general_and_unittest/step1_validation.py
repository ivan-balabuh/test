def check_positive_number(num: int | float):
    # 1. Перевірка через assert (зупинить програму з AssertionError, якщо False)
    assert num > 0, f"Помилка assert: число {num} має бути більшим за 0!"
    
    # 2. Перевірка через ValueError (викидає виняток, який можна перехопити)
    if num > 100:
        raise ValueError(f"Помилка ValueError: число {num} не може бути більшим за 100!")
    
    return f"Число {num} успішно пройшло перевірку!"

if __name__ == "__main__":
    # Правильне введення (запустіть і зробіть скріншот виводу для звіту)
    print(check_positive_number(25))
    print(check_positive_number(-5))    # Викличе AssertionError
    print(check_positive_number(150))   # Викличе ValueError