import tkinter as tk
from tkinter import ttk

    
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
    win.geometry("600x200")
    
def open_quadratic_solver5():
    win = tk.Tk()
    win.title("power")
    win.geometry("600x200")
    
def open_quadratic_solver6(): 
    win = tk.Tk()
    win.title("equations")
    win.geometry("600x200")
    
def open_quadratic_solver7():
    win = tk.Tk()
    win.title("graphs")
    win.geometry("600x200")
      