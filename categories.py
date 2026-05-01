import tkinter as tk
from tkinter import ttk

#Создание кнопок
def add_btns_in_frame(frame):
    frame_name = frame['name']

    if frame_name == "fractions":
        btn1 = ttk.Button(frame, text="Сложение дробей")
        btn1.pack(pady=5, fill='x', padx=20) # fill='x' растянет кнопку по ширине
        
        btn2 = ttk.Button(frame, text="Вычитание дробей")
        btn2.pack(pady=5, fill='x', padx=20)
        
        btn3 = ttk.Button(frame, text="Умножение дробей")
        btn3.pack(pady=5, fill='x', padx=20)
        
        btn4 = ttk.Button(frame, text="Деление дробей")
        btn4.pack(pady=5, fill='x', padx=20)
    
    """match frame['name']:
        case "arithmetic":
            btn1 = ttk.Button(frame, text="+", command=lambda: ("Сложение"))
            btn2 = ttk.Button(frame, text="-", command=lambda: ("Вычитание"))
            btn3 = ttk.Button(frame, text="*", command=lambda: ("Умножение"))
            btn4 = ttk.Button(frame, text="/", command=lambda: ("Деление"))
        case "fractions":
            btn1 = ttk.Button(frame, text="Сложение дробей")
            btn1.pack(pady=5, fill='x', padx=20) # fill='x' растянет кнопку по ширине
            
            btn2 = ttk.Button(frame, text="Вычитание дробей")
            btn2.pack(pady=5, fill='x', padx=20)
            
            btn3 = ttk.Button(frame, text="Умножение дробей")
            btn3.pack(pady=5, fill='x', padx=20)
            
            btn4 = ttk.Button(frame, text="Деление дробей")
            btn4.pack(pady=5, fill='x', padx=20)"""