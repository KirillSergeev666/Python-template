# tasks/task3.py

def solve():
    # Ниже пишите решение задачи
    ticket = input().strip()  # Читаем номер билета
    
    # Проверяем, что билет состоит из 6 цифр
    if len(ticket) != 6 or not ticket.isdigit():
        print("NO")
        return
    
    # Суммируем первые три цифры
    first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    # Суммируем последние три цифры
    last_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    
    # Проверяем, счастливый ли билет
    if first_sum == last_sum:
        print("YES")
    else:
        print("NO")
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()