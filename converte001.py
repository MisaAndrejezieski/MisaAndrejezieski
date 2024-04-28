import tkinter as tk
from tkinter import ttk

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
        result_label.config(text=f"A porcentagem do dia para o tempo {time} é: {percentage}%")

root = tk.Tk()
root.title("Calculadora de Porcentagem do Dia")
root.geometry('300x200')

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="lightblue")
style.configure("TLabel", font=("Arial", 12))

frame = ttk.Frame(root, padding="10")
frame.pack(fill='both', expand=True)

time_label = ttk.Label(frame, text="Por favor, insira o tempo no formato HH:MM")
time_label.pack()

time_entry = ttk.Entry(frame, font=("Arial", 12))
time_entry.pack()

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_percentage)
calculate_button.pack(pady=10)

result_label = ttk.Label(frame, text="")
result_label.pack()

root.mainloop()
