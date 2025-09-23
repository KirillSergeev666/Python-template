# tasks/task2.py

def solve():
# Ниже пишите решение задачи

   x,y,z=map(int,input().split())
   pencil=3
   pen=pencil+2
   flomaster=pen+7
   res=x*pencil+y*pen+z*flomaster
   print(res) 

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()