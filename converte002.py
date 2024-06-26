import tkinter as tk
from tkinter import ttk


def time_to_percentage(time):
    try:
        
        hours, minutes = map(int, time.split(':'))
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError
        total_minutes = hours * 60 + minutes
        percentage = (total_minutes / (24 * 60)) * 100
        return round(percentage, 2)
    except ValueError:
        return None


def calculate_percentage(event=None):
    time = time_entry.get()
    if time:
        percentage = time_to_percentage(time)
        if percentage is not None:
            result_label.config(text=f"A porcentagem do dia para o tempo {time} é: {percentage}%")
        else:
            result_label.config(text="Erro: Por favor, insira o tempo no formato correto (HH:MM).")


root = tk.Tk()
root.title("Calculadora de Porcentagem do Dia")
root.geometry('600x200')

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#1E90FF", foreground="black")
style.configure("TLabel", font=("Arial", 12), background="#F0F8FF")
style.configure("TEntry", font=("Arial", 12))
style.configure(".", background="#F0F8FF")

frame = ttk.Frame(root, padding="30")
frame.pack(fill='both', expand=True)

time_label = ttk.Label(frame, text="Por favor, insira o tempo no formato HH:MM")
time_label.pack()

time_entry = ttk.Entry(frame)
time_entry.pack(pady=10)
time_entry.bind('<Return>', calculate_percentage)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_percentage)
calculate_button.pack(pady=10)

result_label = ttk.Label(frame, text="")
result_label.pack()

root.mainloop()
