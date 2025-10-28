# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    number=int(input())
    hundreds = number // 100          
    tens = (number // 10) % 10        
    units = number % 10  
    print(hundreds+tens+units)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()