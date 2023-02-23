def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if n < 0 :
        raise ValueError("Фактоииал должен вычисялться от не отрицаетльного цисла")
    if not isinstance(n, int):
        raise TypeError("Факториал должен вычисляться от целого цисла")
    if n == 0:
        return 1
    return factorial_recursive(n-1) * n

if __name__ == '__main__':
    value = 3
    print(factorial_recursive(value))