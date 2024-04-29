# Importa os módulos necessários
import tkinter as tk
from tkinter import ttk, messagebox

# Função para converter tempo em porcentagem do dia
def time_to_percentage(time):
    try:
        # Separa as horas e minutos
        hours, minutes = map(int, time.split(":"))
        # Verifica se as horas e minutos são válidos
        if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
            raise ValueError
        # Converte o tempo para minutos
        total_minutes = hours * 60 + minutes
        # Calcula a porcentagem do dia
        percentage = (total_minutes / (24 * 60)) * 100
        return round(percentage, 2)
    except ValueError:
        return None

# Função para calcular a porcentagem do dia com base no tempo inserido
def calculate_percentage(event=None):  # Adicionado parâmetro de evento
    # Obtém o tempo do campo de entrada
    time = time_entry.get()
    # Verifica se o tempo foi inserido
    if not time:
        messagebox.showerror("Erro", "Por favor, insira o tempo no formato HH:MM.")
        return

    try:
        # Calcula a porcentagem do dia
        percentage = time_to_percentage(time)
        if percentage is not None:
            # Atualiza o rótulo do resultado com a porcentagem do dia
            result_label.config(text=f"A porcentagem do dia para {time} é: {percentage}%")
        else:
            messagebox.showerror("Erro", "Formato de tempo inválido. Digite HH:MM.")
    except Exception as e:  # Tratar outras exceções genéricas
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

# Cria a janela principal
root = tk.Tk()
root.title(":: Calculadora de Porcentagem de tempo ::")
root.geometry("600x300")

# Configura o estilo dos widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="orange", foreground="orange")  # Alterado para laranja
style.configure("TEntry", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure(".", background="#87CEFA")  # Alterado para azul clarinho

# Cria um frame para conter os widgets
frame = ttk.Frame(root, padding="30")
frame.pack(fill="both", expand=True)

# Cria um rótulo para instruir o usuário a inserir o tempo
time_label = ttk.Label(frame, text="Digite o tempo no formato HH:MM:")
time_label.pack()

# Cria um campo de entrada para o usuário inserir o tempo
time_entry = ttk.Entry(frame)
time_entry.pack(pady=10)
# Vincula o pressionar Enter à função calculate_percentage
time_entry.bind("<Return>", calculate_percentage)

# Cria um botão para calcular a porcentagem do dia
calculate_button = ttk.Button(frame, text="Pressione Enter", command=calculate_percentage)
calculate_button.pack(pady=10)

# Cria um rótulo para exibir o resultado
result_label = ttk.Label(frame, text="", wraplength=400)  # Permite quebras de linha no texto
result_label.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
