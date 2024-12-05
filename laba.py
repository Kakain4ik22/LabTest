# лаба 1

# print("hello world")

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


# лаба4

# import random
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog

# def create_files():
#     for i in range(1, 4):
#         with open(f'file_{i}.txt', 'w') as f:
#             numbers = [random.randint(1, 100) for _ in range(10)]
#             f.write(' '.join(map(str, numbers)) + '\n')
#     print("Файлы созданы: file_1.txt, file_2.txt, file_3.txt")

# def read_file():

#     filename = filedialog.askopenfile()

#     try:
#         with open(filename.name, 'r') as f:
#             contents = f.readlines()
#             # Преобразуем содержимое в список чисел
#             numbers = [int(num) for line in contents for num in line.split()]
#             average = sum(numbers) / len(numbers) if numbers else 0
#             print(f"Содержимое файла {filename}:")
#             print(' '.join(map(str, numbers)))
#             print(f"Среднее значение: {average}")
#     except FileNotFoundError:
#         print(f"Файл {filename} не найден")
#     except ValueError as e:
#         print(f"Ошибка обработки данных в файле {filename}: {e}")

# def write_to_file():

#     filename = filedialog.askopenfile()

#     numbers = input("Введите числа через пробел для записи в файл: ")
#     numbers_list = list(map(int, numbers.split()))
#     with open(filename.name, 'w') as f:
#         f.write(' '.join(map(str, numbers_list)) + '\n')
#     print(f"Числа записаны в файл {filename}.")

# def main():
#     create_files()

#     while True:
#         action = input("\nВыберите действие: \n1. Прочитать файл \n2. Записать в файл \n3. Выход \nВаш выбор: ")

#         if action == '1':
#             # filename = input("Введите имя файла для чтения: ")
#             read_file()
#         elif action == '2':
#             # filename = input("Введите имя файла для записи: ")
#             write_to_file()
#         elif action == '3':
#             print("Выход из программы")
#             break
#         else:
#             print("Неверный выбор")

# if __name__ == "__main__":
#     main()

# лаба 5

# def say_hello(name):
#     print(f"Привет, {name}!")

# say_hello("Мир")  


# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def make_sound(self):
#         print(f"{self.name} издает звук: {self.sound}")


# cat = Animal("Кошка", "Мяу")
# cat.make_sound()


# class Dog(Animal):
#     def __init__(self, name, sound, breed):
#         super().__init__(name, sound)
#         self.breed = breed

#     def show_breed(self):
#         print(f"Это собака породы: {self.breed}")


# dog = Dog("Собака", "Гав", "Лабрадор")
# dog.make_sound()  # Унаследованный метод
# dog.show_breed()  # Метод второго класса
        
# # лаба 6

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import random

# # Лаба 1: Введение в Python

# def hello_world():

#     """
#     Выводит приветственное сообщение "Hello World" в консоль.
#     """

#     messagebox.showinfo("Сообщение", "Hello World")

# # Лаба 2: Арифметические операции
# def calculate_operations():

#     """
#     Выполняет арифметические операции (сложение, вычитание, умножение, деление и т. д.) над двумя числами,
#     введенными пользователем. Результаты отображаются в окне сообщения.
#     """

#     try:
#         a = int(entry_a.get())
#         b = int(entry_b.get())
#         result = ""

#         result += f"Сложение: {a + b}\n"
#         result += f"Вычитание: {a - b}\n"
#         result += f"Умножение: {a * b}\n"
#         result += f"Возведение в степень: {a ** b}\n"

#         if b == 0:
#             result += "Деление: на ноль делить нельзя\n"
#         else:
#             result += f"Деление: {a / b}\n"
#             result += f"Целочисленное деление: {a // b}\n"

#         messagebox.showinfo("Результаты", result)
#     except ValueError:
#         messagebox.showerror("Ошибка", "Введите корректные числа!")


# # Лаба 3: Работа со списками
# def generate_random_list():

#     """
#     Генерирует случайный список из 10 чисел, вычисляет его сумму, сортирует и находит
#     минимальные и максимальные значения. Результаты отображаются в окне сообщения.
#     """

#     n = [random.randint(0, 10) for _ in range(10)]
#     total_sum = sum(n)
#     sorted_list = sorted(n)
#     reverse_sorted_list = sorted(n, reverse=True)
#     largest = max(n)
#     smallest = min(n)

#     result = f"Список: {n}\n"
#     result += f"Сумма: {total_sum}\n"
#     result += f"Отсортированный: {sorted_list}\n"
#     result += f"Обратная сортировка: {reverse_sorted_list}\n"
#     result += f"Максимум: {largest}\n"
#     result += f"Минимум: {smallest}\n"

#     messagebox.showinfo("Список", result)


# # Лаба 4: Работа с файлами
# def create_files():

#     """
#     Создает три текстовых файла (file_1.txt, file_2.txt, file_3.txt), каждый из которых
#     содержит 10 случайных чисел. Показывает сообщение об успешном создании файлов.
#     """

#     for i in range(1, 4):
#         with open(f'file_{i}.txt', 'w') as f:
#             numbers = [random.randint(1, 100) for _ in range(10)]
#             f.write(' '.join(map(str, numbers)) + '\n')
#     messagebox.showinfo("Файлы", "Созданы файлы: file_1.txt, file_2.txt, file_3.txt")


# def read_file():

#     """
#     Открывает выбранный текстовый файл, считывает его содержимое, вычисляет среднее значение
#     чисел в файле и отображает их в окне сообщения.
#     """

#     filename = filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files", "*.txt")])
#     if not filename:
#         return

#     try:
#         with open(filename, 'r') as f:
#             contents = f.readlines()
#             numbers = [int(num) for line in contents for num in line.split()]
#             average = sum(numbers) / len(numbers) if numbers else 0

#         result = f"Содержимое файла: {numbers}\nСреднее значение: {average}"
#         messagebox.showinfo("Чтение файла", result)
#     except FileNotFoundError:
#         messagebox.showerror("Ошибка", "Файл не найден!")
#     except ValueError as e:
#         messagebox.showerror("Ошибка", f"Ошибка обработки данных: {e}")


# def write_to_file():

#     """
#     Сохраняет введенные пользователем числа в текстовый файл. Если числа не являются
#     корректными, показывает сообщение об ошибке.
#     """

#     filename = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension=".txt",
#                                             filetypes=[("Text files", "*.txt")])
#     if not filename:
#         return

#     numbers = entry_numbers.get()
#     try:
#         numbers_list = list(map(int, numbers.split()))
#         with open(filename, 'a') as f:
#             f.write(' '.join(map(str, numbers_list)) + '\n')
#         messagebox.showinfo("Запись в файл", "Числа успешно записаны!")
#     except ValueError:
#         messagebox.showerror("Ошибка", "Введите корректные числа через пробел!")


# # Лаба 5: Классы и методы
# def show_hello_message():

#     """
#     Показывает приветственное сообщение с именем "Мир".
#     """

#     say_hello("Мир")


# def show_animal_info():

#     """
#     Создает объект класса Animal (Кошка) и показывает сообщение о его звуке.
#     """

#     cat = Animal("Кошка", "Мяу")
#     cat.make_sound()


# def show_dog_info():

#     """
#     Создает объект класса Dog (Собака) и показывает сообщение о его звуке и породе.
#     """

#     dog = Dog("Собака", "Гав", "Лабрадор")
#     dog.make_sound()
#     dog.show_breed()


# # Лаба 5: Классы
# def say_hello(name):

#     """
#     Показывает приветственное сообщение для указанного имени.
    
#     :param name: Имя для приветствия.
#     """

#     messagebox.showinfo("Приветствие", f"Привет, {name}!")


# class Animal:

#     """
#     Класс Animal представляет животное с именем и звуком.
#     """

#     def __init__(self, name, sound):

#         """
#         Создает животное.
        
#         :param name: Имя животного.
#         :param sound: Звук, который издает животное.
#         """

#         self.name = name
#         self.sound = sound

#     def make_sound(self):

#         """
#         Показывает сообщение со звуком, который издает животное.
#         """

#         messagebox.showinfo("Животное", f"{self.name} издает звук: {self.sound}")


# class Dog(Animal):

#     """
#     Класс Dog наследует Animal и добавляет информацию о породе собаки.
#     """

#     def __init__(self, name, sound, breed):

#         """
#         Создает собаку.
        
#         :param name: Имя собаки.
#         :param sound: Звук, который издает собака.
#         :param breed: Порода собаки.
#         """

#         super().__init__(name, sound)
#         self.breed = breed

#     def show_breed(self):

#         """
#         Показывает сообщение с информацией о породе собаки.
#         """

#         messagebox.showinfo("Собака", f"Это собака породы: {self.breed}")


# # Создание GUI
# root = tk.Tk()
# root.title("Лабораторные работы")

# # Лаба 1
# frame_lab1 = tk.LabelFrame(root, text="Лаба 1: Приветственное сообщение")
# frame_lab1.pack(fill="both", expand="yes", padx=10, pady=5)

# tk.Button(frame_lab1, text="Запустить сообщение", command=hello_world).pack()

# # Лаба 2
# frame_lab2 = tk.LabelFrame(root, text="Лаба 2: Арифметические операции")
# frame_lab2.pack(fill="both", expand="yes", padx=10, pady=5)

# tk.Label(frame_lab2, text="Первое число:").pack()
# entry_a = tk.Entry(frame_lab2)
# entry_a.pack()

# tk.Label(frame_lab2, text="Второе число:").pack()
# entry_b = tk.Entry(frame_lab2)
# entry_b.pack()

# tk.Button(frame_lab2, text="Рассчитать", command=calculate_operations).pack()

# # Лаба 3
# frame_lab3 = tk.LabelFrame(root, text="Лаба 3: Работа со списками")
# frame_lab3.pack(fill="both", expand="yes", padx=10, pady=5)

# tk.Button(frame_lab3, text="Сгенерировать список", command=generate_random_list).pack()

# # Лаба 4
# frame_lab4 = tk.LabelFrame(root, text="Лаба 4: Работа с файлами")
# frame_lab4.pack(fill="both", expand="yes", padx=10, pady=5)

# tk.Button(frame_lab4, text="Создать файлы", command=create_files).pack()
# tk.Button(frame_lab4, text="Прочитать файл", command=read_file).pack()

# tk.Label(frame_lab4, text="Введите числа для записи (через пробел):").pack()
# entry_numbers = tk.Entry(frame_lab4)
# entry_numbers.pack()
# tk.Button(frame_lab4, text="Записать в файл", command=write_to_file).pack()

# # Лаба 5
# frame_lab5 = tk.LabelFrame(root, text="Лаба 5: Классы и методы")
# frame_lab5.pack(fill="both", expand="yes", padx=10, pady=5)

# tk.Button(frame_lab5, text="Сказать привет", command=show_hello_message).pack()
# tk.Button(frame_lab5, text="Показать информацию о кошке", command=show_animal_info).pack()
# tk.Button(frame_lab5, text="Показать информацию о собаке", command=show_dog_info).pack()

# root.mainloop()

import requests
from tkinter import Tk, Label

apiKey="7653bfd4f505f804dc6d729e27d99c04"
city="Ulyanovsk"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

def fetch_weather():
    try:
        # Запрос к OpenWeatherMap API
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()

        # Получение температуры
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"Температура в {city}: {temp}°C\nОписание: {description}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка соединения: {e}"
    except KeyError:
        return "Ошибка в данных API!"

# Создание GUI
root = Tk()
root.title("Погода")
root.geometry("300x150")

# Добавление виджета с погодой
weather_label = Label(root, text=fetch_weather(), font=("Arial", 12), justify="left")
weather_label.pack(pady=20)

root.mainloop()