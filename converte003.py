import tkinter as tk
from tkinter import ttk, messagebox

def time_to_percentage(time):
    try:
        hours, minutes = map(int, time.split(":"))
        if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
            raise ValueError
        total_minutes = hours * 60 + minutes
        percentage = (total_minutes / (24 * 60)) * 100
        return round(percentage, 2)
    except ValueError:
        return None

def calculate_percentage(event=None):  # Adicionado parâmetro de evento
    time = time_entry.get()
    if not time:
        messagebox.showerror("Erro", "Por favor, insira o tempo no formato HH:MM.")
        return

    try:
        percentage = time_to_percentage(time)
        if percentage is not None:
            result_label.config(text=f"A porcentagem do dia para {time} é: {percentage}%")
        else:
            messagebox.showerror("Erro", "Formato de tempo inválido. Digite HH:MM.")
    except Exception as e:  # Tratar outras exceções genéricas
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title(":: Calculadora de Porcentagem de tempo ::")
root.geometry("600x300")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="	# FF6347", foreground="black")  # Alterado para verde
style.configure("TEntry", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure(".", background="# 87CEFA")  # Alterado para vermelho

frame = ttk.Frame(root, padding="30")
frame.pack(fill="both", expand=True)

time_label = ttk.Label(frame, text="Digite o tempo no formato HH:MM:")
time_label.pack()

time_entry = ttk.Entry(frame)
time_entry.pack(pady=10)
time_entry.bind("<Return>", calculate_percentage)  # Vincular o pressionar Enter à função calculate_percentage

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_percentage)
calculate_button.pack(pady=10)

result_label = ttk.Label(frame, text="", wraplength=400)  # Permite quebras de linha no texto
result_label.pack(pady=10)

root.mainloop()
