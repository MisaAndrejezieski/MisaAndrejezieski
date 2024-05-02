import tkinter as tk
# Função para calcular e mostrar os números pares
def calcular_numeros():
    try:
        # Obtendo o número limite e o intervalo a partir das entradas do usuário
        limite = int(entry_limite.get())
        intervalo = int(entry_intervalo.get())

        # Verificando se o intervalo é positivo
        if intervalo <= 0:
            label_resultado['text'] = "O intervalo deve ser um número positivo."
            return

        # Calculando os números pares dentro do intervalo especificado
        numeros_pares = [n for n in range(0, limite + 1, intervalo) if n % 2 == 0]
        
        # Atualizando o texto do label com os resultados
        label_resultado['text'] = f"Números pares até {limite} (de {intervalo} em {intervalo}): {numeros_pares}"
    except ValueError:
        # Caso a entrada não seja um número inteiro válido
        label_resultado['text'] = "Por favor, insira números inteiros válidos."

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Números Pares")

# Configuração do layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Entrada para o número limite
label_limite = tk.Label(frame, text="Insira o número limite:")
label_limite.pack()
entry_limite = tk.Entry(frame)
entry_limite.pack()

# Entrada para o intervalo
label_intervalo = tk.Label(frame, text="Insira o intervalo:")
label_intervalo.pack()
entry_intervalo = tk.Entry(frame)
entry_intervalo.pack()

# Botão para calcular os números
botao_calcular = tk.Button(frame, text="Calcular Números", command=calcular_numeros)
botao_calcular.pack()

# Label para mostrar o resultado
label_resultado = tk.Label(frame, text="")
label_resultado.pack()

# Iniciar a aplicação
root.mainloop()
