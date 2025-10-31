# tasks/task1.py

def solve():
    # Ниже пишите решение задачи
    number = int(input())  # Читаем число
    total = 0
    
    # Находим сумму цифр числа
    while number > 0:
        digit = number % 10  # Получаем последнюю цифру
        total += digit       # Добавляем к сумме
        number //= 10       # Убираем последнюю цифру
    
    print(total)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()