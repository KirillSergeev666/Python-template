# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n=int(input())
    hours = n // 3600 % 24
    minutes = (n // 60) % 60
    seconds = n % 60
    print(f"{hours}:{minutes:02d}:{seconds:02d}")


   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()