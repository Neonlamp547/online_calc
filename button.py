import tkinter as tk
from tkinter import ttk
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk, messagebox

    
def open_quadratic_solver():
    win = tk.Tk()
    win.title("fractions")
    win.geometry("600x200")
    
def open_summ():
    win = tk.Tk()
    win.title("Сложение")
    win.geometry("600x200")
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    win.resizable(False, False)
    
    eq_frame = ttk.Frame(main_frame)
    eq_frame.pack(pady=30)
    
    entry1 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry1.grid(row=0, column=0, padx=5)
    entry1.insert(0, "")  # Значение по умолчанию
    
    # Знак плюс
    lbl_plus = ttk.Label(eq_frame, text="+", font=("Arial", 16, "bold"))
    lbl_plus.grid(row=0, column=1, padx=5)
    
    # Второе число
    entry2 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry2.grid(row=0, column=2, padx=5)
    entry2.insert(0, "")  # Значение по умолчанию
    
    # Знак равно
    btn_equals = ttk.Button(
        eq_frame, 
        text="=", 
        width=3,
        style='TButton'
    )
    btn_equals.grid(row=0, column=3, padx=3)
    
    # Поле результата (только для чтения)
    entry_result = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center', state='readonly')
    entry_result.grid(row=0, column=4, padx=5)
    
    # Функция вычисления
    def calculate_sum():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 + num2
            
            # Форматируем результат
            if result == int(result):
                result_text = str(int(result))
            else:
                result_text = f"{result:.2f}"
            
            # Обновляем поле результата
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result_text)
            entry_result.config(state='readonly')
            
        except ValueError:
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка")
            entry_result.config(state='readonly')
    
    btn_equals.config(command=calculate_sum)

def open_minus():
    win = tk.Tk()
    win.title("Вычитание")
    win.geometry("600x200")
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    win.resizable(False, False)
    
    eq_frame = ttk.Frame(main_frame)
    eq_frame.pack(pady=30)
    
    entry1 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry1.grid(row=0, column=0, padx=5)
    entry1.insert(0, "")  # Значение по умолчанию
    
    # Знак минус
    lbl_minus = ttk.Label(eq_frame, text="-", font=("Arial", 16, "bold"))
    lbl_minus.grid(row=0, column=1, padx=5)
    
    # Второе число
    entry2 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry2.grid(row=0, column=2, padx=5)
    entry2.insert(0, "")  # Значение по умолчанию
    
    # Знак равно
    btn_equals = ttk.Button(
        eq_frame, 
        text="=", 
        width=3,
        style='TButton'
    )
    btn_equals.grid(row=0, column=3, padx=3)
    
    # Поле результата (только для чтения)
    entry_result = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center', state='readonly')
    entry_result.grid(row=0, column=4, padx=5)
    
    # Функция вычисления
    def calculate_min():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 - num2
            
            # Форматируем результат
            if result == int(result):
                result_text = str(int(result))
            else:
                result_text = f"{result:.2f}"
            
            # Обновляем поле результата
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result_text)
            entry_result.config(state='readonly')
            
        except ValueError:
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка")
            entry_result.config(state='readonly')
    
    btn_equals.config(command=calculate_min)
    
def open_umn():
    win = tk.Tk()
    win.title("Умножение")
    win.geometry("600x200")
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    win.resizable(False, False)
    
    eq_frame = ttk.Frame(main_frame)
    eq_frame.pack(pady=30)
    
    entry1 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry1.grid(row=0, column=0, padx=5)
    entry1.insert(0, "")  # Значение по умолчанию
    
    # Знак умножения
    lbl_minus = ttk.Label(eq_frame, text="*", font=("Arial", 16, "bold"))
    lbl_minus.grid(row=0, column=1, padx=5)
    
    # Второе число
    entry2 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry2.grid(row=0, column=2, padx=5)
    entry2.insert(0, "")  # Значение по умолчанию
    
    # Знак равно
    btn_equals = ttk.Button(
        eq_frame, 
        text="=", 
        width=3,
        style='TButton'
    )
    btn_equals.grid(row=0, column=3, padx=3)
    
    # Поле результата (только для чтения)
    entry_result = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center', state='readonly')
    entry_result.grid(row=0, column=4, padx=5)
    
    # Функция вычисления
    def calculate_umn():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 * num2
            
            # Форматируем результат
            if result == int(result):
                result_text = str(int(result))
            else:
                result_text = f"{result:.2f}"
            
            # Обновляем поле результата
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result_text)
            entry_result.config(state='readonly')
            
        except ValueError:
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка")
            entry_result.config(state='readonly')
    
    btn_equals.config(command=calculate_umn)
    
def open_del():
    win = tk.Tk()
    win.title("Деление")
    win.geometry("600x200")
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    win.resizable(False, False)
    
    eq_frame = ttk.Frame(main_frame)
    eq_frame.pack(pady=30)
    
    entry1 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry1.grid(row=0, column=0, padx=5)
    entry1.insert(0, "")  # Значение по умолчанию
    
    # Знак деления
    lbl_minus = ttk.Label(eq_frame, text="//", font=("Arial", 16, "bold"))
    lbl_minus.grid(row=0, column=1, padx=5)
    
    # Второе число
    entry2 = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center')
    entry2.grid(row=0, column=2, padx=5)
    entry2.insert(0, "")  # Значение по умолчанию
    
    # Знак равно
    btn_equals = ttk.Button(
        eq_frame, 
        text="=", 
        width=3,
        style='TButton'
    )
    btn_equals.grid(row=0, column=3, padx=3)
    
    # Поле результата (только для чтения)
    entry_result = ttk.Entry(eq_frame, width=8, font=("Arial", 16), justify='center', state='readonly')
    entry_result.grid(row=0, column=4, padx=5)
    
    # Функция вычисления
    def calculate_del():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 // num2
            
            # Форматируем результат
            if result == int(result):
                result_text = str(int(result))
            else:
                result_text = f"{result:.2f}"
            
            # Обновляем поле результата
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result_text)
            entry_result.config(state='readonly')
            
        except ValueError:
            entry_result.config(state='normal')
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка")
            entry_result.config(state='readonly')
    
    btn_equals.config(command=calculate_del)
    
def open_quadratic_solver3():
    win = tk.Tk()
    win.title("square_roots")
    win.geometry("600x200")
    
    
def open_quadratic_solver4():
    win = tk.Tk()
    win.title("percentages")
    win.geometry("600x400")
def open_percent_calculator():
    """
    Открывает окно для расчета процентов:
    Находит X% от числа Y.
    """
    
    win = tk.Toplevel()
    win.title("Калькулятор процентов")
    win.geometry("400x350")
    win.resizable(False, False)
    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Найти процент от числа", font=("Arial", 12, "bold")).pack(pady=10)
    
    # Поля ввода
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(pady=10, fill='x')
    
    # Число
    row_num = ttk.Frame(input_frame)
    row_num.pack(fill='x', pady=5)
    ttk.Label(row_num, text="Число:", width=10).pack(side='left')
    entry_num = ttk.Entry(row_num, width=15)
    entry_num.pack(side='left', padx=5)
    entry_num.insert(0, "") # Пример по умолчанию
    
    # Процент
    row_pct = ttk.Frame(input_frame)
    row_pct.pack(fill='x', pady=5)
    ttk.Label(row_pct, text="Процент (%):", width=10).pack(side='left')
    entry_pct = ttk.Entry(row_pct, width=15)
    entry_pct.pack(side='left', padx=5)
    entry_pct.insert(0, "") # Пример по умолчанию
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ", command=lambda: calculate_percent())
    btn_solve.pack(pady=15, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Результат", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 14, "bold"), foreground="blue", anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_percent():
        try:
            number = float(entry_num.get())
            percent = float(entry_pct.get())
            
            # Формула: (Число * Процент) / 100
            result = (number * percent) / 100
            
            # Форматируем вывод
            if result == int(result):
                res_text = str(int(result))
            else:
                res_text = f"{result:.4f}"
                
            lbl_result.config(text=f"{percent}% от {number} = {res_text}", foreground="green")
            
        except ValueError:
            lbl_result.config(text="Ошибка ввода!", foreground="red")
            
    # Фокус на первое поле
    entry_num.focus_set()
    
    # Расчет по Enter
    entry_num.bind('<Return>', lambda e: calculate_percent())
    entry_pct.bind('<Return>', lambda e: calculate_percent())

def open_add_percent():
    """
    Открывает окно для прибавления процента к числу:
    Число + (Число * Процент / 100)
    """
    
    win = tk.Toplevel()
    win.title("Прибавление процента")
    win.geometry("400x350")
    win.resizable(False, False)
    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Прибавить % к числу", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(main_frame, text="(Например: 1000 + 13%)", foreground="#666").pack()
    
    # Поля ввода
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(pady=15, fill='x')
    
    # Исходное число
    row_num = ttk.Frame(input_frame)
    row_num.pack(fill='x', pady=5)
    ttk.Label(row_num, text="Число:", width=12).pack(side='left')
    entry_num = ttk.Entry(row_num, width=15)
    entry_num.pack(side='left', padx=5)
    entry_num.insert(0, "")
    
    # Процент
    row_pct = ttk.Frame(input_frame)
    row_pct.pack(fill='x', pady=5)
    ttk.Label(row_pct, text="Процент (%):", width=12).pack(side='left')
    entry_pct = ttk.Entry(row_pct, width=15)
    entry_pct.pack(side='left', padx=5)
    entry_pct.insert(0, "")
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ (+%)", command=lambda: calculate_add_percent())
    btn_solve.pack(pady=15, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Итоговое значение", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 14, "bold"), foreground="darkgreen", anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_add_percent():
        try:
            number = float(entry_num.get())
            percent = float(entry_pct.get())
            
            # Формула: Число + (Число * Процент / 100)
            # Или проще: Число * (1 + Процент/100)
            added_value = (number * percent) / 100
            final_result = number + added_value
            
            # Форматируем вывод
            if final_result == int(final_result):
                res_text = str(int(final_result))
                add_text = str(int(added_value))
            else:
                res_text = f"{final_result:.2f}"
                add_text = f"{added_value:.2f}"
                
            lbl_result.config(
                text=f"{number} + {percent}% = {res_text}\n(Прибавлено: {add_text})", 
                foreground="darkgreen"
            )
            
        except ValueError:
            lbl_result.configtext="Ошибка ввода"
            
import tkinter as tk
from tkinter import ttk, messagebox

def open_subtract_percent():
    """
    Открывает окно для вычитания процента из числа:
    Число - (Число * Процент / 100)
    """
    
    win = tk.Toplevel()
    win.title("Вычитание процента")
    win.geometry("400x350")
    win.resizable(False, False)
    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Вычесть % из числа", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(main_frame, text="(Например: 1000 - 20% скидка)", foreground="#666").pack()
    
    # Поля ввода
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(pady=15, fill='x')
    
    # Исходное число
    row_num = ttk.Frame(input_frame)
    row_num.pack(fill='x', pady=5)
    ttk.Label(row_num, text="Число:", width=12).pack(side='left')
    entry_num = ttk.Entry(row_num, width=15)
    entry_num.pack(side='left', padx=5)
    entry_num.insert(0, "")
    
    # Процент
    row_pct = ttk.Frame(input_frame)
    row_pct.pack(fill='x', pady=5)
    ttk.Label(row_pct, text="Процент (%):", width=12).pack(side='left')
    entry_pct = ttk.Entry(row_pct, width=15)
    entry_pct.pack(side='left', padx=5)
    entry_pct.insert(0, "")
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ (-%)", command=lambda: calculate_sub_percent())
    btn_solve.pack(pady=15, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Итоговое значение", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 14, "bold"), foreground="darkred", anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_sub_percent():
        try:
            number = float(entry_num.get())
            percent = float(entry_pct.get())
            
            # Формула: Число - (Число * Процент / 100)
            subtracted_value = (number * percent) / 100
            final_result = number - subtracted_value
            
            # Форматируем вывод
            if final_result == int(final_result):
                res_text = str(int(final_result))
                sub_text = str(int(subtracted_value))
            else:
                res_text = f"{final_result:.2f}"
                sub_text = f"{subtracted_value:.2f}"
                
            lbl_result.config(
                text=f"{number} - {percent}% = {res_text}\n(Вычтено: {sub_text})", 
                foreground="darkred"
            )
            
        except ValueError:
            lbl_result.config(text="Ошибка ввода!", foreground="red")
            
    # Фокус и Enter
    entry_num.focus_set()
    entry_num.bind('<Return>', lambda e: calculate_sub_percent())
    entry_pct.bind('<Return>', lambda e: calculate_sub_percent())
    
def open_power_calculator():
    """
    Открывает окно для возведения числа в степень:
    Основание ^ Показатель степени
    """
    win = tk.Tk()
    win.title("power")
    win.geometry("500x400")

    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Возведение в степень", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(main_frame, text="Формат: Основание ^ Степень", foreground="#666").pack()
    
    # Поля ввода
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(pady=15, fill='x')
    
    # Основание (число)
    row_base = ttk.Frame(input_frame)
    row_base.pack(fill='x', pady=5)
    ttk.Label(row_base, text="Основание:", width=12).pack(side='left')
    entry_base = ttk.Entry(row_base, width=15)
    entry_base.pack(side='left', padx=5)
    entry_base.insert(0, "") # Пример по умолчанию
    
    # Показатель степени
    row_exp = ttk.Frame(input_frame)
    row_exp.pack(fill='x', pady=5)
    ttk.Label(row_exp, text="Степень:", width=12).pack(side='left')
    entry_exp = ttk.Entry(row_exp, width=15)
    entry_exp.pack(side='left', padx=5)
    entry_exp.insert(0, "") # Пример по умолчанию
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ (^)", command=lambda: calculate_power())
    btn_solve.pack(pady=55, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Результат", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 14, "bold"), foreground="purple", anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_power():
        try:
            base = float(entry_base.get())
            exponent = float(entry_exp.get())
            
            # Проверка на сложные случаи (например, отрицательное основание и дробная степень)
            if base < 0 and exponent != int(exponent):
                # Если основание отрицательное, а степень дробная (корень из отрицательного), 
                # результат будет комплексным числом. Python это поддерживает, но выведем аккуратно.
                result = complex(base) ** exponent
                # Форматируем комплексное число
                res_text = f"{result.real:.4f} + {result.imag:.4f}i"
                lbl_result.config(text=f"{base} ^ {exponent} =\n{res_text}", foreground="purple")
            else:
                result = base ** exponent
                
                # Если результат очень большой или очень маленький, используем научную нотацию
                if abs(result) > 1e9 or (abs(result) < 1e-6 and result != 0):
                    res_text = f"{result:.4e}"
                elif result == int(result):
                    res_text = str(int(result))
                else:
                    res_text = f"{result:.6f}"
                    
                lbl_result.config(text=f"{base} ^ {exponent} = {res_text}", foreground="purple")
            
        except ValueError:
            lbl_result.config(text="Ошибка ввода!", foreground="red")
        except OverflowError:
            lbl_result.config(text="Число слишком велико!", foreground="red")
            
    # Фокус и Enter
    entry_base.focus_set()
    entry_base.bind('<Return>', lambda e: calculate_power())
    entry_exp.bind('<Return>', lambda e: calculate_power())
    
def open_add_powers():
    """
    Открывает окно для сложения двух степеней:
    (Основание1 ^ Показатель1) + (Основание2 ^ Показатель2)
    """
    
    win = tk.Toplevel()
    win.title("Сложение степеней")
    win.geometry("600x500")
    win.resizable(False, False)
    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Сложение степеней", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(main_frame, text="Формула: aⁿ + b", foreground="#666").pack()
    
    # --- Первая степень ---
    frame_pow1 = ttk.LabelFrame(main_frame, text="Первая степень (aⁿ)", padding=10)
    frame_pow1.pack(fill='x', pady=10)
    
    row_a = ttk.Frame(frame_pow1)
    row_a.pack(fill='x', pady=2)
    ttk.Label(row_a, text="Основание (a):", width=15).pack(side='left')
    entry_base1 = ttk.Entry(row_a, width=10)
    entry_base1.pack(side='left', padx=5)
    entry_base1.insert(0, "")
    
    row_n = ttk.Frame(frame_pow1)
    row_n.pack(fill='x', pady=2)
    ttk.Label(row_n, text="Показатель (n):", width=15).pack(side='left')
    entry_exp1 = ttk.Entry(row_n, width=10)
    entry_exp1.pack(side='left', padx=5)
    entry_exp1.insert(0, "")
    
    # --- Вторая степень ---
    frame_pow2 = ttk.LabelFrame(main_frame, text="Вторая степень (bᵐ)", padding=10)
    frame_pow2.pack(fill='x', pady=10)
    
    row_b = ttk.Frame(frame_pow2)
    row_b.pack(fill='x', pady=2)
    ttk.Label(row_b, text="Основание (b):", width=15).pack(side='left')
    entry_base2 = ttk.Entry(row_b, width=10)
    entry_base2.pack(side='left', padx=5)
    entry_base2.insert(0, "")
    
    row_m = ttk.Frame(frame_pow2)
    row_m.pack(fill='x', pady=2)
    ttk.Label(row_m, text="Показатель (m):", width=15).pack(side='left')
    entry_exp2 = ttk.Entry(row_m, width=10)
    entry_exp2.pack(side='left', padx=5)
    entry_exp2.insert(0, "")
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ (+)", command=lambda: calculate_sum_powers())
    btn_solve.pack(pady=15, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Результат", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 12), justify='center', anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_sum_powers():
        try:
            # Получаем данные
            a = float(entry_base1.get())
            n = float(entry_exp1.get())
            b = float(entry_base2.get())
            m = float(entry_exp2.get())
            
            # Вычисляем степени
            val1 = a ** n
            val2 = b ** m
            
            # Складываем
            total = val1 + val2
            
            # Форматируем вывод
            # Если числа целые и небольшие, показываем как int
            def fmt(x):
                return str(int(x)) if x == int(x) else f"{x:.4f}"
                
            res_text = (
                f"1-я степень: {fmt(a)}^{fmt(n)} = {fmt(val1)}\n"
                f"2-я степень: {fmt(b)}^{fmt(m)} = {fmt(val2)}\n"
                f"--------------------------\n"
                f"Сумма: {fmt(total)}"
            )
            
            lbl_result.config(text=res_text, foreground="darkblue")
            
        except ValueError:
            lbl_result.config(text="Ошибка ввода!\nВведите числа.", foreground="red")
        except OverflowError:
            lbl_result.config(text="Число слишком большое!", foreground="red")
            
    # Фокус и Enter
    entry_base1.focus_set()
    # Привязка Enter ко всем полям для удобства
    for e in [entry_base1, entry_exp1, entry_base2, entry_exp2]:
        e.bind('<Return>', lambda e: calculate_sum_powers())

def open_power_subtraction():
    """
    Открывает окно для вычисления разности степеней:
    (Основание1 ^ Показатель1) - (Основание2 ^ Показатель2)
    """
    
    win = tk.Toplevel()
    win.title("Вычитание степеней")
    win.geometry("600x500")
    win.resizable(False, False)
    
    # Основной фрейм
    main_frame = ttk.Frame(win, padding=20)
    main_frame.pack(fill='both', expand=True)
    
    # Заголовок
    ttk.Label(main_frame, text="Вычисление: Aˣ - Bʸ", font=("Arial", 12, "bold")).pack(pady=10)
    
    # --- Первая степень (A^x) ---
    frame_pow1 = ttk.LabelFrame(main_frame, text="Первое число (Aˣ)", padding=10)
    frame_pow1.pack(fill='x', pady=5)
    
    row_a = ttk.Frame(frame_pow1)
    row_a.pack(fill='x', pady=2)
    ttk.Label(row_a, text="Основание (A):", width=15).pack(side='left')
    entry_base1 = ttk.Entry(row_a, width=10)
    entry_base1.pack(side='left', padx=5)
    entry_base1.insert(0, "")
    
    row_x = ttk.Frame(frame_pow1)
    row_x.pack(fill='x', pady=2)
    ttk.Label(row_x, text="Показатель (x):", width=15).pack(side='left')
    entry_exp1 = ttk.Entry(row_x, width=10)
    entry_exp1.pack(side='left', padx=5)
    entry_exp1.insert(0, "")
    
    # Знак минуса между блоками
    lbl_minus = ttk.Label(main_frame, text="−", font=("Arial", 16, "bold"))
    lbl_minus.pack(pady=5)
    
    # --- Вторая степень (B^y) ---
    frame_pow2 = ttk.LabelFrame(main_frame, text="Второе число (Bʸ)", padding=10)
    frame_pow2.pack(fill='x', pady=5)
    
    row_b = ttk.Frame(frame_pow2)
    row_b.pack(fill='x', pady=2)
    ttk.Label(row_b, text="Основание (B):", width=15).pack(side='left')
    entry_base2 = ttk.Entry(row_b, width=10)
    entry_base2.pack(side='left', padx=5)
    entry_base2.insert(0, "")
    
    row_y = ttk.Frame(frame_pow2)
    row_y.pack(fill='x', pady=2)
    ttk.Label(row_y, text="Показатель (y):", width=15).pack(side='left')
    entry_exp2 = ttk.Entry(row_y, width=10)
    entry_exp2.pack(side='left', padx=5)
    entry_exp2.insert(0, "")
    
    # Кнопка Решить
    btn_solve = ttk.Button(main_frame, text="РЕШИТЬ (Aˣ - Bʸ)", command=lambda: calculate_power_diff())
    btn_solve.pack(pady=15, fill='x')
    
    # Поле результата
    result_frame = ttk.LabelFrame(main_frame, text="Результат", padding=10)
    result_frame.pack(fill='both', expand=True, pady=5)
    
    lbl_result = ttk.Label(result_frame, text="...", font=("Arial", 14, "bold"), foreground="blue", anchor='center')
    lbl_result.pack(expand=True)
    
    def calculate_power_diff():
        try:
            # Получаем значения
            base1 = float(entry_base1.get())
            exp1 = float(entry_exp1.get())
            base2 = float(entry_base2.get())
            exp2 = float(entry_exp2.get())
            
            # Вычисляем степени
            val1 = math.pow(base1, exp1)
            val2 = math.pow(base2, exp2)
            
            # Вычитаем
            result = val1 - val2
            
            # Форматируем вывод
            if result == int(result):
                res_text = str(int(result))
            else:
                res_text = f"{result:.4f}"
                
            # Показываем промежуточные вычисления для наглядности
            detail_text = f"({base1}^{exp1}) - ({base2}^{exp2})\n= {val1:g} - {val2:g}\n= {res_text}"
            
            lbl_result.config(text=detail_text, foreground="blue")
            
        except ValueError:
            lbl_result.config(text="Ошибка ввода!", foreground="red")
        except OverflowError:
            lbl_result.config(text="Число слишком большое!", foreground="red")
            
    # Фокус и Enter
    entry_base1.focus_set()
    # Привязка Enter ко всем полям для удобства
    for entry in [entry_base1, entry_exp1, entry_base2, entry_exp2]:
        entry.bind('<Return>', lambda e: calculate_power_diff())

def open_linear_equation_solver():
    """Открывает окно для решения линейного уравнения ax + b = 0 с графиком"""
    
    # Создаем дочернее окно
    win = tk.Toplevel()
    win.title("Линейное уравнение: ax + b = 0")
    win.geometry("600x500")
    
    # === ВЕРХНЯЯ ЧАСТЬ: ВВОД И РЕШЕНИЕ ===
    input_frame = ttk.Frame(win, padding=15)
    input_frame.pack(fill='x', pady=10)
    
    # Заголовок
    ttk.Label(input_frame, text="Решение уравнения: ax + b = 0", 
              font=("Arial", 14, "bold")).pack(pady=(0, 15))
    
    # Поля ввода a и b
    coeffs_frame = ttk.Frame(input_frame)
    coeffs_frame.pack(pady=5)
    
    ttk.Label(coeffs_frame, text="a =", font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky='e')
    entry_a = ttk.Entry(coeffs_frame, width=8, font=("Arial", 12))
    entry_a.grid(row=0, column=1, padx=5)
    entry_a.insert(0, "")  # Пример по умолчанию
    
    ttk.Label(coeffs_frame, text="b =", font=("Arial", 12)).grid(row=0, column=2, padx=5, sticky='e')
    entry_b = ttk.Entry(coeffs_frame, width=8, font=("Arial", 12))
    entry_b.grid(row=0, column=3, padx=5)
    entry_b.insert(0, "")  # Пример по умолчанию
    
    # Кнопка "Решить"
    btn_solve = ttk.Button(
        input_frame, 
        text="Решить", 
        width=15,
        style='Accent.TButton'
    )
    btn_solve.pack(pady=15)
    
    # Поле для вывода ответа
    result_label = ttk.Label(
        input_frame, 
        text="", 
        font=("Arial", 13, "bold"),
        foreground="green",
        justify='center'
    )
    result_label.pack(pady=10)
    
    # === НИЖНЯЯ ЧАСТЬ: ГРАФИК ===
    graph_frame = ttk.LabelFrame(win, text="График функции y = ax + b", padding=10)
    graph_frame.pack(fill='both', expand=True, padx=15, pady=10)
    
    # Функция решения и построения графика
    def solve_and_plot():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            
            # --- РЕШЕНИЕ УРАВНЕНИЯ ---
            if a == 0:
                if b == 0:
                    answer = "Любое x (0 = 0)"
                    color = "blue"
                else:
                    answer = "Нет решений"
                    color = "red"
            else:
                x_root = -b / a
                # Форматируем ответ
                if x_root == int(x_root):
                    answer = f"x = {int(x_root)}"
                else:
                    answer = f"x = {x_root:.4f}"
                color = "green"
            
            result_label.config(text=answer, foreground=color)
            
            # --- ПОСТРОЕНИЕ ГРАФИКА ---
            # Очищаем старый график
            for widget in graph_frame.winfo_children():
                widget.destroy()
            
            # Создаем фигуру matplotlib
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            
            # Генерируем данные для графика
            x_range = np.linspace(-10, 10, 400)
            y_values = a * x_range + b
            
            # Строим линию функции
            ax.plot(x_range, y_values, 'b-', linewidth=2, label=f'y = {a}x + {b}')
            
            # Если есть корень, отмечаем его на графике
            if a != 0:
                x_root = -b / a
                ax.axvline(x=x_root, color='red', linestyle='--', alpha=0.7, 
                          label=f'Корень: x={x_root:.2f}')
                ax.plot(x_root, 0, 'ro', markersize=8, zorder=5)
            
            # Оси координат
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            
            # Сетка и легенда
            ax.grid(True, alpha=0.3)
            ax.legend(loc='best')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title(f'График: y = {a}x + {b}')
            
            # Встраиваем график в Tkinter
            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
        except ValueError:
            result_label.config(text="Ошибка: введите числа!", foreground="red")
            # Очищаем график при ошибке
            for widget in graph_frame.winfo_children():
                widget.destroy()
            ttk.Label(graph_frame, text="Невозможно построить график", 
                     foreground="red").pack(expand=True)
    
    # Привязываем функцию к кнопке
    btn_solve.config(command=solve_and_plot)
    
    # Также решаем по нажатию Enter
    entry_a.bind('<Return>', lambda e: solve_and_plot())
    entry_b.bind('<Return>', lambda e: solve_and_plot())
    
    # Фокус на первое поле
    entry_a.focus_set()
    
    # Автоматически решаем при открытии окна (опционально)
    win.after(100, solve_and_plot)
    


def open_quadratic_solver_with_graph():
    """
    Открывает окно для решения квадратного уравнения ax² + bx + c = 0
    С полями ввода, кнопкой "Решить" и построением графика.
    """
    
    # 1. Создаем главное дочернее окно
    win = tk.Toplevel()
    win.title("Квадратное уравнение")
    win.geometry("800x600")
    
    # --- Верхняя часть: Ввод и Результат ---
    top_frame = ttk.Frame(win)
    top_frame.pack(fill='x', padx=20, pady=10)
    
    lbl_title = ttk.Label(top_frame, text="Решение: ax² + bx + c = 0", font=("Arial", 14, "bold"))
    lbl_title.pack(pady=5)
    
    # Поля ввода a, b, c
    input_frame = ttk.Frame(top_frame)
    input_frame.pack(pady=10)
    
    ttk.Label(input_frame, text="a =", width=5).grid(row=0, column=0, padx=5)
    entry_a = ttk.Entry(input_frame, width=10)
    entry_a.grid(row=0, column=1, padx=5)
    entry_a.insert(0, "")
    
    ttk.Label(input_frame, text="b =", width=5).grid(row=0, column=2, padx=5)
    entry_b = ttk.Entry(input_frame, width=10)
    entry_b.grid(row=0, column=3, padx=5)
    entry_b.insert(0, "")
    
    ttk.Label(input_frame, text="c =", width=5).grid(row=0, column=4, padx=5)
    entry_c = ttk.Entry(input_frame, width=10)
    entry_c.grid(row=0, column=5, padx=5)
    entry_c.insert(0, "")
    
    # Кнопка Решить
    btn_solve = ttk.Button(top_frame, text="РЕШИТЬ", style='Accent.TButton')
    btn_solve.pack(pady=10)
    
    # Лейбл для текстового ответа
    lbl_answer = ttk.Label(top_frame, text="", font=("Arial", 12), justify='left', foreground="blue")
    lbl_answer.pack(pady=5)
    
    # --- Нижняя часть: График ---
    graph_frame = ttk.LabelFrame(win, text="График функции y = ax² + bx + c", padding=10)
    graph_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    def solve_and_plot():
        try:
            # Получаем коэффициенты
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            
            if a == 0:
                lbl_answer.config(text="Ошибка: 'a' не может быть равно 0 (это не квадратное уравнение)", foreground="red")
                return
            
            # 1. Математическое решение
            D = b**2 - 4*a*c
            answer_text = f"Дискриминант D = {D}\n\n"
            
            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2*a)
                x2 = (-b - math.sqrt(D)) / (2*a)
                # Красивое форматирование
                x1_str = int(x1) if x1 == int(x1) else round(x1, 3)
                x2_str = int(x2) if x2 == int(x2) else round(x2, 3)
                answer_text += f"D > 0 → Два корня:\nx₁ = {x1_str}\nx₂ = {x2_str}"
            elif D == 0:
                x = -b / (2*a)
                x_str = int(x) if x == int(x) else round(x, 3)
                answer_text += f"D = 0 → Один корень:\nx = {x_str}"
            else:
                answer_text += f"D < 0 → Действительных корней нет."
                
            lbl_answer.config(text=answer_text, foreground="black")
            
            # 2. Построение графика
            # Очищаем старый график
            for widget in graph_frame.winfo_children():
                widget.destroy()
                
            # Генерируем данные для графика
            # Берем диапазон вокруг вершины параболы или корней
            vertex_x = -b / (2*a)
            range_val = max(abs(vertex_x) * 2 + 5, 10) # Динамический диапазон
            x_vals = np.linspace(vertex_x - range_val, vertex_x + range_val, 400)
            y_vals = a * x_vals**2 + b * x_vals + c
            
            # Создаем фигуру Matplotlib
            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)
            
            # Рисуем параболу
            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'y = {a}x² + {b}x + {c}')
            
            # Рисуем оси
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            
            # Если есть корни, отмечаем их на графике
            if D >= 0:
                if D > 0:
                    ax.plot([x1, x2], [0, 0], 'ro', markersize=8, label='Корни')
                else:
                    ax.plot([x], [0, 0], 'ro', markersize=8, label='Корень')
                    
            # Настройки графика
            ax.grid(True, alpha=0.3)
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.legend()
            ax.set_title("График квадратичной функции")
            
            # Встраиваем график в Tkinter
            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
        except ValueError:
            lbl_answer.config(text="Ошибка: Введите корректные числа!", foreground="red")
        except Exception as e:
            lbl_answer.config(text=f"Произошла ошибка: {e}", foreground="red")

    # Привязываем функцию к кнопке
    btn_solve.config(command=solve_and_plot)
    
    # Сразу строим график для значений по умолчанию
    solve_and_plot()
    

def open_biquadratic_solver():
    """Открывает окно для решения биквадратного уравнения ax⁴ + bx² + c = 0"""
    
    win = tk.Toplevel()
    win.title("Биквадратное уравнение")
    win.geometry("600x700")
    
    # Заголовок
    lbl_title = ttk.Label(win, text="Решение: ax⁴ + bx² + c = 0", font=("Arial", 14, "bold"))
    lbl_title.pack(pady=15)
    
    # Поля ввода коэффициентов
    input_frame = ttk.Frame(win)
    input_frame.pack(pady=10)
    
    ttk.Label(input_frame, text="a =").grid(row=0, column=0, padx=5, sticky='e')
    entry_a = ttk.Entry(input_frame, width=10)
    entry_a.grid(row=0, column=1, padx=5)
    entry_a.insert(0, "")
    
    ttk.Label(input_frame, text="b =").grid(row=1, column=0, padx=5, sticky='e')
    entry_b = ttk.Entry(input_frame, width=10)
    entry_b.grid(row=1, column=1, padx=5)
    entry_b.insert(0, "")
    
    ttk.Label(input_frame, text="c =").grid(row=2, column=0, padx=5, sticky='e')
    entry_c = ttk.Entry(input_frame, width=10)
    entry_c.grid(row=2, column=1, padx=5)
    entry_c.insert(0, "")
    
    # Кнопка "Решить"
    btn_solve = ttk.Button(win, text="Решить", command=lambda: solve_biquadratic(entry_a, entry_b, entry_c, result_label, plot_frame))
    btn_solve.pack(pady=15)
    
    # Метка для вывода результатов
    result_label = ttk.Label(win, text="", font=("Arial", 11), justify='left', foreground="green")
    result_label.pack(pady=10)
    
    # Фрейм для графика
    plot_frame = ttk.Frame(win)
    plot_frame.pack(fill='both', expand=True, padx=20, pady=10)


def solve_biquadratic(entry_a, entry_b, entry_c, result_label, plot_frame):
    """Решает биквадратное уравнение и строит график"""
    
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        if a == 0:
            result_label.config(text="Ошибка: a не может быть равно 0!", foreground="red")
            return
        
        # Решаем квадратное уравнение относительно y = x²: a*y² + b*y + c = 0
        D = b**2 - 4*a*c
        
        roots_x = []  # Корни исходного уравнения
        
        if D < 0:
            result_text = f"D = {D} < 0 → Нет действительных корней у вспомогательного уравнения.\nНет решений."
        elif D == 0:
            y = -b / (2*a)
            if y < 0:
                result_text = f"D = 0, y = {y} < 0 → Нет действительных корней x."
            elif y == 0:
                roots_x = [0.0]
                result_text = f"D = 0, y = 0 → x = 0"
            else:
                sqrt_y = np.sqrt(y)
                roots_x = [-sqrt_y, sqrt_y]
                result_text = f"D = 0, y = {y} → x₁ = {-sqrt_y:.4f}, x₂ = {sqrt_y:.4f}"
        else:  # D > 0
            y1 = (-b + np.sqrt(D)) / (2*a)
            y2 = (-b - np.sqrt(D)) / (2*a)
            
            temp_roots = []
            for y in [y1, y2]:
                if y > 0:
                    sqrt_y = np.sqrt(y)
                    temp_roots.extend([-sqrt_y, sqrt_y])
                elif y == 0:
                    temp_roots.append(0.0)
                # если y < 0 — пропускаем
            
            if not temp_roots:
                result_text = f"D = {D}, но оба корня y < 0 → Нет действительных корней x."
            else:
                # Убираем дубликаты и сортируем
                roots_x = sorted(set(temp_roots))
                result_text = f"D = {D}\ny₁ = {y1:.4f}, y₂ = {y2:.4f}\nКорни x: "
                for i, root in enumerate(roots_x, 1):
                    result_text += f"x{i} = {root:.4f}  "
        
        result_label.config(text=result_text, foreground="green")
        
        # --- Построение графика ---
        # Очищаем старый график
        for widget in plot_frame.winfo_children():
            widget.destroy()
        
        # Создаём функцию f(x) = a*x^4 + b*x^2 + c
        x_vals = np.linspace(-3, 3, 1000)
        y_vals = a * x_vals**4 + b * x_vals**2 + c
        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f"f(x) = {a}x⁴ + {b}x² + {c}")
        ax.axhline(0, color='black', linewidth=0.8)
        ax.axvline(0, color='black', linewidth=0.8)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("График биквадратной функции")
        ax.legend()
        
        # Отмечаем корни на графике
        for root in roots_x:
            ax.plot(root, 0, 'ro', markersize=8)  # Красные точки на оси X
        
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
    except Exception as e:
        result_label.config(text=f"Ошибка: {str(e)}", foreground="red")
        # Очищаем график при ошибке
        for widget in plot_frame.winfo_children():
            widget.destroy()

def open_linear_inequality_solver():
    """Открывает окно для решения линейного неравенства ax + b > 0 (или <, >=, <=)"""
    
    win = tk.Toplevel()
    win.title("Линейное неравенство")
    win.geometry("800x600")
    
    # --- Верхняя панель: Ввод данных ---
    input_frame = ttk.LabelFrame(win, text="Введите коэффициенты", padding=10)
    input_frame.pack(fill='x', padx=10, pady=10)
    
    # Ряд 1: Коэффициенты a и b
    coeff_frame = ttk.Frame(input_frame)
    coeff_frame.pack(pady=5)
    
    ttk.Label(coeff_frame, text="a =").grid(row=0, column=0, padx=5)
    entry_a = ttk.Entry(coeff_frame, width=10)
    entry_a.grid(row=0, column=1, padx=5)
    entry_a.insert(0, "")
    
    ttk.Label(coeff_frame, text="b =").grid(row=0, column=2, padx=5)
    entry_b = ttk.Entry(coeff_frame, width=10)
    entry_b.grid(row=0, column=3, padx=5)
    entry_b.insert(0, "")
    
    # Ряд 2: Выбор знака неравенства
    sign_var = tk.StringVar(value=">")
    sign_frame = ttk.Frame(input_frame)
    sign_frame.pack(pady=5)
    
    ttk.Label(sign_frame, text="Знак:").pack(side='left', padx=5)
    ttk.Radiobutton(sign_frame, text=">", variable=sign_var, value=">").pack(side='left')
    ttk.Radiobutton(sign_frame, text="<", variable=sign_var, value="<").pack(side='left')
    ttk.Radiobutton(sign_frame, text="≥", variable=sign_var, value=">=").pack(side='left')
    ttk.Radiobutton(sign_frame, text="≤", variable=sign_var, value="<=").pack(side='left')
    
    # Кнопка Решить
    btn_solve = ttk.Button(input_frame, text="Решить", command=lambda: solve_and_plot())
    btn_solve.pack(pady=10)
    
    # --- Нижняя часть: Результат и График ---
    bottom_frame = ttk.Frame(win)
    bottom_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Левая часть: Текстовый ответ
    result_frame = ttk.LabelFrame(bottom_frame, text="Ответ", padding=10, width=200)
    result_frame.pack(side='left', fill='y', padx=(0, 10))
    
    lbl_answer = ttk.Label(result_frame, text="Нажмите 'Решить'", wraplength=180, justify='center')
    lbl_answer.pack(expand=True)
    
    # Правая часть: График Matplotlib
    plot_frame = ttk.LabelFrame(bottom_frame, text="График f(x) = ax + b", padding=5)
    plot_frame.pack(side='right', fill='both', expand=True)
    
    def solve_and_plot():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            sign = sign_var.get()
            
            if a == 0:
                lbl_answer.config(text="Ошибка: a не может быть равно 0", foreground="red")
                return
            
            # 1. Математическое решение
            # ax + b > 0  =>  ax > -b
            # Если a > 0: x > -b/a
            # Если a < 0: x < -b/a (знак меняется при делении на отрицательное)
            
            root_x = -b / a
            
            if sign in [">", ">="]:
                if a > 0:
                    sol_str = f"x {sign} {root_x:g}"
                    interval = f"({root_x:g}; +∞)" if sign == ">" else f"[{root_x:g}; +∞)"
                else:
                    # Знак инвертируется
                    new_sign = "<" if sign == ">" else "<="
                    sol_str = f"x {new_sign} {root_x:g}"
                    interval = f"(-∞; {root_x:g})" if new_sign == "<" else f"(-∞; {root_x:g}]"
            else: # < or <=
                if a > 0:
                    sol_str = f"x {sign} {root_x:g}"
                    interval = f"(-∞; {root_x:g})" if sign == "<" else f"(-∞; {root_x:g}]"
                else:
                    new_sign = ">" if sign == "<" else ">="
                    sol_str = f"x {new_sign} {root_x:g}"
                    interval = f"({root_x:g}; +∞)" if new_sign == ">" else f"[{root_x:g}; +∞)"

            answer_text = f"Корень уравнения ax+b=0:\nx₀ = {root_x:g}\n\nРешение неравенства:\n{sol_str}\n\nИнтервал:\n{interval}"
            lbl_answer.config(text=answer_text, foreground="green")
            
            # 2. Построение графика
            for widget in plot_frame.winfo_children():
                widget.destroy()
                
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            
            # Диапазон X
            x_range = 10 if abs(root_x) < 5 else abs(root_x) * 2
            x_vals = np.linspace(root_x - x_range, root_x + x_range, 400)
            y_vals = a * x_vals + b
            
            ax.plot(x_vals, y_vals, label=f'f(x) = {a}x + {b}', color='blue', linewidth=2)
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.grid(True, alpha=0.3)
            
            # Закраска области решения
            # Мы закрашиваем там, где график выше или ниже оси X в зависимости от знака
            if sign in [">", ">="]:
                # Нам нужно f(x) > 0 (выше оси X)
                ax.fill_between(x_vals, y_vals, 0, where=(y_vals > 0), interpolate=True, color='green', alpha=0.3, label='Решение (>0)')
            else:
                # Нам нужно f(x) < 0 (ниже оси X)
                ax.fill_between(x_vals, y_vals, 0, where=(y_vals < 0), interpolate=True, color='red', alpha=0.3, label='Решение (<0)')
                
            # Точка корня
            ax.plot(root_x, 0, 'ro', markersize=8, label=f'Корень ({root_x:g}; 0)')
            
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.legend(loc='upper left')
            ax.set_title(f"График решения: {sol_str}")
            
            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
        except ValueError:
            lbl_answer.config(text="Ошибка ввода!", foreground="red")
        except Exception as e:
            lbl_answer.config(text=f"Ошибка: {e}", foreground="red")

    # Инициализация пустого графика при открытии
    solve_and_plot()


def open_quadratic_inequality():
    """
    Открывает окно для решения квадратного неравенства ax² + bx + c > 0 (или <, >=, <=)
    С выводом ответа и графика.
    """
    
    win = tk.Toplevel()
    win.title("Квадратное неравенство")
    win.geometry("800x600")
    
    # --- Левая панель: Ввод и Ответ ---
    left_frame = ttk.Frame(win, width=300)
    left_frame.pack(side='left', fill='y', padx=10, pady=10)
    left_frame.pack_propagate(False) # Фиксируем ширину
    
    ttk.Label(left_frame, text="Решение неравенства:", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(left_frame, text="Формат: ax² + bx + c  ?  0", foreground="#555").pack()
    
    # Поля ввода коэффициентов
    input_frame = ttk.Frame(left_frame)
    input_frame.pack(pady=15, fill='x')
    
    # Коэффициент a
    row_a = ttk.Frame(input_frame)
    row_a.pack(fill='x', pady=2)
    ttk.Label(row_a, text="a =", width=5).pack(side='left')
    entry_a = ttk.Entry(row_a, width=10)
    entry_a.pack(side='left', padx=5)
    entry_a.insert(0, "")
    
    # Коэффициент b
    row_b = ttk.Frame(input_frame)
    row_b.pack(fill='x', pady=2)
    ttk.Label(row_b, text="b =", width=5).pack(side='left')
    entry_b = ttk.Entry(row_b, width=10)
    entry_b.pack(side='left', padx=5)
    entry_b.insert(0, "")
    
    # Коэффициент c
    row_c = ttk.Frame(input_frame)
    row_c.pack(fill='x', pady=2)
    ttk.Label(row_c, text="c =", width=5).pack(side='left')
    entry_c = ttk.Entry(row_c, width=10)
    entry_c.pack(side='left', padx=5)
    entry_c.insert(0, "")
    
    # Выбор знака неравенства
    sign_var = tk.StringVar(value=">")
    sign_frame = ttk.Frame(left_frame)
    sign_frame.pack(pady=10, fill='x')
    ttk.Label(sign_frame, text="Знак:").pack(side='left', padx=5)
    
    signs = [">", "<", ">=", "<="]
    for s in signs:
        ttk.Radiobutton(sign_frame, text=s, variable=sign_var, value=s).pack(side='left', padx=2)
        
    # Кнопка Решить
    btn_solve = ttk.Button(left_frame, text="РЕШИТЬ", command=lambda: solve_and_plot())
    btn_solve.pack(pady=20, fill='x')
    
    # Область вывода текста
    text_frame = ttk.LabelFrame(left_frame, text="Ответ", padding=10)
    text_frame.pack(fill='both', expand=True, pady=10)
    
    result_text = tk.Text(text_frame, height=10, wrap='word', font=("Consolas", 11))
    result_text.pack(fill='both', expand=True)
    
    # --- Правая панель: График ---
    right_frame = ttk.Frame(win)
    right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
    
    # Контейнер для графика matplotlib
    plot_container = ttk.Frame(right_frame)
    plot_container.pack(fill='both', expand=True)
    
    def solve_and_plot():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            sign = sign_var.get()
            
            if a == 0:
                messagebox.showerror("Ошибка", "Коэффициент 'a' не может быть равен 0 (это не квадратное неравенство)")
                return
            
            # Очистка предыдущего графика и текста
            for widget in plot_container.winfo_children():
                widget.destroy()
            result_text.delete(1.0, tk.END)
            
            # 1. Математическая часть
            D = b**2 - 4*a*c
            x_vertex = -b / (2*a)
            y_vertex = a * x_vertex**2 + b * x_vertex + c
            
            info = f"Парабола: y = {a}x² + {b}x + {c}\n"
            info += f"Вершина параболы: ({x_vertex:.2f}; {y_vertex:.2f})\n\n"
            
            roots = []
            if D > 0:
                x1 = (-b - np.sqrt(D)) / (2*a)
                x2 = (-b + np.sqrt(D)) / (2*a)
                roots = [x1, x2]
                info += f"Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}\n"
            elif D == 0:
                x1 = -b / (2*a)
                roots = [x1]
                info += f"Один корень (касание): x = {x1:.2f}\n"
            else:
                info += "Действительных корней нет.\n"
                
            # Определение интервалов
            solution_str = ""
            if D > 0:
                r1, r2 = sorted(roots)
                if sign in [">", ">="]:
                    if a > 0:
                        sol = f"x ∈ (-∞; {r1:.2f}) ∪ ({r2:.2f}; +∞)"
                        if sign == ">=": sol = f"x ∈ (-∞; {r1:.2f}] ∪ [{r2:.2f}; +∞)"
                    else:
                        sol = f"x ∈ [{r1:.2f}; {r2:.2f}]" if sign == ">=" else f"x ∈ ({r1:.2f}; {r2:.2f})"
                else: # < or <=
                    if a > 0:
                        sol = f"x ∈ [{r1:.2f}; {r2:.2f}]" if sign == "<=" else f"x ∈ ({r1:.2f}; {r2:.2f})"
                    else:
                        sol = f"x ∈ (-∞; {r1:.2f}) ∪ ({r2:.2f}; +∞)"
                        if sign == "<=": sol = f"x ∈ (-∞; {r1:.2f}] ∪ [{r2:.2f}; +∞)"
                solution_str = f"\nРешение неравенства:\n{sol}"
            elif D == 0:
                r = roots[0]
                if sign in [">", ">="]:
                     sol = f"x ≠ {r}" if sign == ">" else "Любое число"
                     if a < 0: sol = "Нет решений" if sign == ">" else f"x = {r}"
                else:
                     sol = f"x = {r}" if sign == "<" else "Любое число"
                     if a > 0: sol = "Нет решений" if sign == "<" else f"x = {r}"
                solution_str = f"\nРешение неравенства:\n{sol}"
            else:
                if sign in [">", ">="]:
                    sol = "Любое число" if a > 0 else "Нет решений"
                else:
                    sol = "Нет решений" if a > 0 else "Любое число"
                solution_str = f"\nРешение неравенства:\n{sol}"

            result_text.insert(tk.END, info + solution_str)
            
            # 2. Построение графика
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            
            # Диапазон X
            x_min = min(roots) - 5 if roots else x_vertex - 5
            x_max = max(roots) + 5 if roots else x_vertex + 5
            if not roots: 
                x_min, x_max = x_vertex - 5, x_vertex + 5
                
            x_vals = np.linspace(x_min, x_max, 400)
            y_vals = a * x_vals**2 + b * x_vals + c
            
            # Основная линия параболы
            ax.plot(x_vals, y_vals, label=f'y = {a}x²+{b}x+{c}', color='blue', linewidth=2)
            
            # Закраска области решения
            # Создаем маску для заливки
            if sign in [">", ">="]:
                condition = y_vals > 0 if sign == ">" else y_vals >= 0
                if a < 0: condition = ~condition # Если ветви вниз, то решение там, где y < 0
            else: # < or <=
                condition = y_vals < 0 if sign == "<" else y_vals <= 0
                if a < 0: condition = ~condition
                
            # Простой способ заливки: fill_between
            # Если корни есть, заливаем между ними или вне их
            if D > 0:
                r1, r2 = sorted(roots)
                if (a > 0 and sign in ['<', '<=']) or (a < 0 and sign in ['>', '>=']):
                    # Заливка МЕЖДУ корнями
                    ax.fill_between(x_vals, y_vals, 0, where=(x_vals >= r1) & (x_vals <= r2), alpha=0.3, color='green')
                else:
                    # Заливка ВНЕ корней
                    ax.fill_between(x_vals, y_vals, 0, where=(x_vals <= r1) | (x_vals >= r2), alpha=0.3, color='green')
            elif D == 0:
                 pass # Точечное касание сложно красиво залить без шума, оставим линию
            else:
                if (a > 0 and sign in ['>', '>=']) or (a < 0 and sign in ['<', '<=']):
                    ax.axhspan(min(y_vals), max(y_vals), alpha=0.2, color='green') # Вся плоскость
                else:
                    pass # Нет решений или вся плоскость (зависит от знака)

            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.set_title("График функции и область решения")
            ax.legend()
            
            canvas = FigureCanvasTkAgg(fig, master=plot_container)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    # Запуск расчета при открытии (опционально)
    # solve_and_plot() 
    
def open_quadratic_solver7():
    win = tk.Tk()
    win.title("graphs")
    win.geometry("600x200")
    
    

      