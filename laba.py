# лаба 2

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))


# if(b == 0):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a**b)
#     print("на ноль делить нельзя")
# else:
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a**b)
#     print(a/b)
#     print(a//b)

# лаба 3

# import random

# n = []
# j = 10


# total_sum = 0


# for i in range(j):
#     n.append(random.randint(0, 10))
#     total_sum += i
# print(n)
# print(total_sum)

# n.sort()

# print(n)
# print(n[-1])

# print(sorted(n,reverse=True))
# print(n[0])


#лаба 4

import random

def create_files():
    for i in range(1, 4):
        with open(f'file_{i}.txt', 'w') as f:
            numbers = [random.randint(1, 100) for _ in range(10)]
            f.write(' '.join(map(str, numbers)) + '\n')
    print("Файлы созданы: file_1.txt, file_2.txt, file_3.txt")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.readlines()
            # Преобразуем содержимое в список чисел
            numbers = [int(num) for line in contents for num in line.split()]
            average = sum(numbers) / len(numbers) if numbers else 0
            print(f"Содержимое файла {filename}:")
            print(' '.join(map(str, numbers)))
            print(f"Среднее значение: {average}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except ValueError as e:
        print(f"Ошибка обработки данных в файле {filename}: {e}")

def write_to_file(filename):
    numbers = input("Введите числа через пробел для записи в файл: ")
    numbers_list = list(map(int, numbers.split()))
    with open(filename, 'a') as f:
        f.write(' '.join(map(str, numbers_list)) + '\n')
    print(f"Числа записаны в файл {filename}.")

def main():
    create_files()

    while True:
        action = input("\nВыберите действие: \n1. Прочитать файл \n2. Записать в файл \n3. Выход \nВаш выбор: ")

        if action == '1':
            filename = input("Введите имя файла для чтения: ")
            read_file(filename)
        elif action == '2':
            filename = input("Введите имя файла для записи: ")
            write_to_file(filename)
        elif action == '3':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
        


