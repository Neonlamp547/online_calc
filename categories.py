import tkinter as tk
from tkinter import ttk
from button import open_quadratic_solver
from button import open_quadratic_solver2
from button import open_quadratic_solver3
from button import open_quadratic_solver4
from button import open_quadratic_solver5
from button import open_quadratic_solver6
from button import open_quadratic_solver7

#Создание кнопок
def add_btns_in_frame(frame,category_name,):
    

    if  category_name == "fractions":
        btn1 = ttk.Button(frame, text="Сложение дробей", padding=(10,30), command=open_quadratic_solver)
        btn1.pack(pady=5, fill='x', padx=20) # fill='x' растянет кнопку по ширине
        
        btn2 = ttk.Button(frame, text="Вычитание дробей", padding=(10,30),command=open_quadratic_solver)
        btn2.pack(pady=5, fill='x', padx=20)
    
        btn3 = ttk.Button(frame, text="Умножение дробей", padding=(10,30),command=open_quadratic_solver)
        btn3.pack(pady=5, fill='x', padx=20)
        
        btn4 = ttk.Button(frame, text="Деление дробей", padding=(10,30),command=open_quadratic_solver)
        btn4.pack(pady=5, fill='x', padx=20)
    
    elif  category_name == "arithmetic":
     
            btn1 = ttk.Button(frame, text= "Сложение", padding=(10,30),)
            btn1.pack(pady=5, fill='x', padx=20)
            btn2 = ttk.Button(frame, text="-", command=lambda: "Вычитание", padding=(10,30))
            btn2.pack(pady=5, fill='x', padx=20)
            btn3 = ttk.Button(frame, text="*", command=lambda: "Умножение", padding=(10,30))
            btn3.pack(pady=5, fill='x', padx=20)
            btn4 = ttk.Button(frame, text="/", command=lambda: "Деление", padding=(10,30),)
            btn4.pack(pady=5, fill='x', padx=20)
    elif category_name == "square_roots":
        
        btn1 = ttk.Button(frame, text="Извлечение корня", command=lambda: "Извлечение корня", padding=(10,30))
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение корней", command=lambda: "Сложение корней", padding=(10,30))
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание корней", command=lambda: "Вычитание корней", padding=(10,30))
        btn3.pack(pady=5, fill='x', padx=20)
        btn4 = ttk.Button(frame, text="Умножение корней", command=lambda: "Умножение корней", padding=(10,30))
        btn4.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Деление корней", command=lambda: "Деление корней", padding=(10,30))
        btn5.pack(pady=5, fill='x', padx=20)
        
    elif category_name == "percentages":
        btn1 = ttk.Button(frame, text="Проценты", command=lambda: "Проценты", padding=(10,30))
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение процентов", command=lambda: "Вычитание процентов", padding=(10,30))
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание процентов", command=lambda: "Сложение процентов", padding=(10,30))
        btn3.pack(pady=5, fill='x', padx=20)
        
        
    elif category_name == "power":
        
        btn1 = ttk.Button(frame, text="Возведение в степень", command=lambda: "Возведение в степень", padding=(10,30))
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение степеней", command=lambda: "Сложение степеней", padding=(10,30))
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание степеней", command=lambda: "Вычитание степеней", padding=(10,30))
        btn3.pack(pady=5, fill='x', padx=20)
        btn4 = ttk.Button(frame, text="Умножение степеней", command=lambda: "Умножение степеней", padding=(10,30))
        btn4.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Деление степеней", command=lambda: "Деление степеней", padding=(10,30))
        btn5.pack(pady=5, fill='x', padx=20)
        
        
    elif category_name == "graphs":
        btn1 = ttk.Button(frame, text="Прямая", command=lambda: "Линейная", padding=(10,30))
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Гипербола", command=lambda: "Гипербола", padding=(10,30))
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Пораболы", command=lambda: "Порабала", padding=(10,30))
        btn3.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Ветвь пораболы", command=lambda: "Ветвь пораболы", padding=(10,30))
        btn5.pack(pady=5, fill='x', padx=20)
        
    elif category_name == "equations":
        btn1 = ttk.Button(frame, text="Линейное уравнение", command=lambda: "Линейное", padding=(10,30))
        btn1.pack(pady=5, fill='x', padx=20)
        
        btn2 = ttk.Button(frame, text="Квадратное уравнение", command=lambda: "Квадратное", padding=(10,30))
        btn2.pack(pady=5, fill='x', padx=20)
        
        btn3 = ttk.Button(frame, text="Биквадратное уравнение", command=lambda: "Биквадратное", padding=(10,30))
        btn3.pack(pady=5, fill='x', padx=20)
        
        btn4 = ttk.Button(frame, text="Линейное неравенство", command=lambda: "Линейное нер-во", padding=(10,30))
        btn4.pack(pady=5, fill='x', padx=20)
        
        btn5 = ttk.Button(frame, text="Квадратное неравенство", command=lambda: "Квадратное нер-во", padding=(10,30))
        btn5.pack(pady=5, fill='x', padx=20)