def processar_reservas():

    confirmadas = []
    recusadas = []

    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    for q in reservas_solicitadas:
        if q in quartos_disponiveis:
            confirmadas.append(q)
        else:
            recusadas.append(q)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()