import tkinter as tk
from tkinter import ttk
from button import open_quadratic_solver
from button import open_summ
from button import open_minus
from button import open_umn
from button import open_del
from button import open_quadratic_solver3
from button import open_quadratic_solver4
from button import open_quadratic_solver5
from button import open_quadratic_solver6
from button import open_quadratic_solver7

#Создание кнопок
def add_btns_in_frame(frame,category_name):
    

    if  category_name == "fractions":
        btn1 = ttk.Button(frame, text="Сложение дробей", padding=(10,30), command=open_quadratic_solver)
        btn1.pack(pady=5, fill='x', padx=20) # fill='x' растянет кнопку по ширине
        
        btn2 = ttk.Button(frame, text="Вычитание дробей", padding=(10,30), command=open_quadratic_solver)
        btn2.pack(pady=5, fill='x', padx=20)
    
        btn3 = ttk.Button(frame, text="Умножение дробей", padding=(10,30), command=open_quadratic_solver)
        btn3.pack(pady=5, fill='x', padx=20)
        
        btn4 = ttk.Button(frame, text="Деление дробей", padding=(10,30), command=open_quadratic_solver)
        btn4.pack(pady=5, fill='x', padx=20)
        
    elif  category_name == "arithmetic":
     
        btn1 = ttk.Button(frame, text="Сложение", padding=(10,30), command=open_summ)
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Вычитание", padding=(10,30), command=open_minus)
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Умножение", padding=(10,30), command=open_umn)
        btn3.pack(pady=5, fill='x', padx=20)
        btn4 = ttk.Button(frame, text="Деление", padding=(10,30), command=open_del)
        btn4.pack(pady=5, fill='x', padx=20)
    
    
            
            
    elif category_name == "square_roots":
        
        btn1 = ttk.Button(frame, text="Извлечение корня", padding=(10,30), command=open_quadratic_solver3)
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение корней", padding=(10,30), command=open_quadratic_solver3)
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание корней", padding=(10,30), command=open_quadratic_solver3)
        btn3.pack(pady=5, fill='x', padx=20)
        btn4 = ttk.Button(frame, text="Умножение корней", padding=(10,30), command=open_quadratic_solver3)
        btn4.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Деление корней", padding=(10,30), command=open_quadratic_solver3)
        btn5.pack(pady=5, fill='x', padx=20)
        
    elif category_name == "percentages":
        btn1 = ttk.Button(frame, text="Проценты", padding=(10,30), command=open_quadratic_solver4)
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение процентов", padding=(10,30), command=open_quadratic_solver4)
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание процентов", padding=(10,30), command=open_quadratic_solver4)
        btn3.pack(pady=5, fill='x', padx=20)
        
        
    elif category_name == "power":
        
        btn1 = ttk.Button(frame, text="Возведение в степень", padding=(10,30), command=open_quadratic_solver5)
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Сложение степеней", padding=(10,30), command=open_quadratic_solver5)
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Вычитание степеней", padding=(10,30), command=open_quadratic_solver5)
        btn3.pack(pady=5, fill='x', padx=20)
        btn4 = ttk.Button(frame, text="Умножение степеней", padding=(10,30), command=open_quadratic_solver5)
        btn4.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Деление степеней", padding=(10,30), command=open_quadratic_solver5)
        btn5.pack(pady=5, fill='x', padx=20)
        
        
    elif category_name == "graphs":
        btn1 = ttk.Button(frame, text="Прямая", padding=(10,30), command=open_quadratic_solver6)
        btn1.pack(pady=5, fill='x', padx=20)
        btn2 = ttk.Button(frame, text="Гипербола", padding=(10,30), command=open_quadratic_solver6)
        btn2.pack(pady=5, fill='x', padx=20)
        btn3 = ttk.Button(frame, text="Пораболы", padding=(10,30), command=open_quadratic_solver6)
        btn3.pack(pady=5, fill='x', padx=20)
        btn5 = ttk.Button(frame, text="Ветвь пораболы", padding=(10,30), command=open_quadratic_solver6)
        btn5.pack(pady=5, fill='x', padx=20)
        
    elif category_name == "equations":
        btn1 = ttk.Button(frame, text="Линейное уравнение", padding=(10,30), command=open_quadratic_solver7)
        btn1.pack(pady=5, fill='x', padx=20)
        
        btn2 = ttk.Button(frame, text="Квадратное уравнение", padding=(10,30), command=open_quadratic_solver7)
        btn2.pack(pady=5, fill='x', padx=20)
        
        btn3 = ttk.Button(frame, text="Биквадратное уравнение", padding=(10,30), command=open_quadratic_solver7)
        btn3.pack(pady=5, fill='x', padx=20)
        
        btn4 = ttk.Button(frame, text="Линейное неравенство", padding=(10,30), command=open_quadratic_solver7)
        btn4.pack(pady=5, fill='x', padx=20)
        
        btn5 = ttk.Button(frame, text="Квадратное неравенство", padding=(10,30), command=open_quadratic_solver7)
        btn5.pack(pady=5, fill='x', padx=20)