import tkinter as tk
from tkinter import messagebox

def time_to_percentage(time):
    # Converte o tempo no formato HH:MM para uma porcentagem do dia
    hours, minutes = map(int, time.split(':'))
    total_minutes = hours * 60 + minutes
    percentage = (total_minutes / (24 * 60)) * 100
    return round(percentage, 2)

def calculate_percentage():
    time = time_entry.get()
    if time:
        percentage = time_to_percentage(time)
        messagebox.showinfo("Resultado", f"A porcentagem do dia para o tempo {time} é: {percentage}%")

root = tk.Tk()
root.title("Calculadora de Porcentagem do Dia")

time_label = tk.Label(root, text="Por favor, insira o tempo no formato HH:MM")
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

calculate_button = tk.Button(root, text="Calcular", command=calculate_percentage)
calculate_button.pack()

root.mainloop()
