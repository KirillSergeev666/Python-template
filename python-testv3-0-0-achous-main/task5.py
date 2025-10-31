# tasks/task5.py

def solve():
    # Ниже пишите решение задачи
    # Читаем входные данные: текущее время и минуты для прибавления
    hours = int(input())
    minutes = int(input())
    add_minutes = int(input())
    
    # Переводим всё в минуты
    total_minutes = hours * 60 + minutes + add_minutes
    
    # Вычисляем новые часы и минуты
    new_hours = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60
    
    # Выводим результат в формате ЧЧ:ММ
    print(f"{new_hours:02d} {new_minutes:02d}")
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()