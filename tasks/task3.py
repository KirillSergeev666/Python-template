# tasks/task3.py

def solve():
# Ниже пишите решение задачи

    a, b = map(int, input().split())
    not_shot_by_harry = b - 1
    not_shot_by_larry = a - 1
    print(not_shot_by_harry, not_shot_by_larry)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()