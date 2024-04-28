def time_to_percentage(time):
    # Converte o tempo no formato HH:MM para uma porcentagem do dia
    hours, minutes = map(int, time.split(':'))
    total_minutes = hours * 60 + minutes
    percentage = (total_minutes / (24 * 60)) * 100
    return round(percentage, 2)

def main():
    while True:
        time = input("Por favor, insira o tempo no formato HH:MM (ou 'sair' para terminar): ")
        if time.lower() == 'sair':
            break
        percentage = time_to_percentage(time)
        print(f"A porcentagem do dia para o tempo {time} é: {percentage}%")

if _name_ == "_main_":
    main()