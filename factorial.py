def factorial(n):
    # Задаём условия выхода из рекурсии:
    if n==0: return 1
    if n==1: return 1
    # Во всех других случаях возвращаем
    # произведение текущего числа n и функции от n-1
    return factorial(n-1)*n
print(factorial(322))