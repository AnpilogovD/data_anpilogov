def fib(n):
    # Задаём условия выхода из рекурсии:
    if n == 0: return 0
    if n == 1: return 1
    # Возвращаемое значение согласно рекурсивной функции:
    return fib(n-1) + fib(n-2)
  print(fib(44))