import tkinter as tk
from tkinter import ttk
from categories import add_btns_in_frame

window = tk.Tk()
window.title("Онлайн кальулятор")
window.geometry("800x550")
window.resizable(False,False)

#Создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill='both')

#Создаем фрейм
frame1 = ttk.Frame(notebook, name="arithmetic")
frame2 = ttk.Frame(notebook, name="fractions")
frame3 = ttk.Frame(notebook, name="square_roots")
frame4 = ttk.Frame(notebook, name="percentages")
frame5 = ttk.Frame(notebook, name="power")
frame6 = ttk.Frame(notebook, name="equations")
frame7 = ttk.Frame(notebook, name="graphs")

#Добавляем вкладок
notebook.add(frame1, text="Арифметика")
notebook.add(frame2, text="Обыкновенные дроби")
notebook.add(frame3, text="Квадратные корни")
notebook.add(frame4, text="Проценты")
notebook.add(frame5, text="Возведение в степень")
notebook.add(frame6, text="Уравнения и неравенства")
notebook.add(frame7, text="Графики функций")

add_btns_in_frame(frame1, "arithmetic")
add_btns_in_frame(frame2, "fractions")
add_btns_in_frame(frame3, "square_roots")
add_btns_in_frame(frame4, "percentages")
add_btns_in_frame(frame7, "graphs")
add_btns_in_frame(frame5, "power" )
add_btns_in_frame(frame6, "equations" )

window.mainloop()