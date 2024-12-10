def ancient_cipher(n):
    if not (3 <= n <= 20):
        return "Число должно быть в диапазоне от 3 до 20."
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += f"{i}{j}"
    return result
n = int(input("Введите число (от 3 до 20): "))
print("Результат:", ancient_cipher(n))