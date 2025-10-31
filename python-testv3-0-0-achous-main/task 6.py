# tasks/task7.py

def solve():
    # Задание №2 Шифр данных
    number = input().strip()
    
    # Преобразуем каждую цифру в число
    digits = [int(digit) for digit in number]
    
    # Шаг 1: Заменить каждую цифру значением (цифра + 7) % 10
    encrypted_digits = []
    for digit in digits:
        new_digit = (digit + 7) % 10
        encrypted_digits.append(new_digit)
    
    # Шаг 2: Поменять местами первую цифру и третью, вторую и четвёртую
    # Индексы: 0-первая, 1-вторая, 2-третья, 3-четвёртая
    encrypted_digits[0], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[0]
    encrypted_digits[1], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[1]
    
    # Собираем результат
    result = ''.join(str(digit) for digit in encrypted_digits)
    print(result)

if __name__ == "__main__":
    solve()
    git clone
    git status
    git add <Кирилл сергеев и206а>
    git commit -m"дз"
    git push origin main


