

def factorial_iterative(n: int) -> int:
    """
    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    result = 1
    # Проверяем на отрицательные параметры.
    if n < 0:
        raise ValueError("Факториал считается от неотрицательных целых чисел")
    # Факториал 0 равен 1 по определению.
    if n == 0:
        return result
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == '__main__':
    n = 10
    print(factorial_iterative(n))

