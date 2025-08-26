
#Função criada para priorizar o atendimento
def ordem_atendimento(n):  
    # Lista para armazenar pacientes
    pacientes = []
     # Loop para entrada de dados
    for _ in range(n):
        nome, idade, status = input("Nome, idade, status do paciente: ").strip().split(", ")
        idade = int(idade)
        pacientes.append((nome, idade, status))
  
    # TODO: Ordene por prioridade: urgente > idosos > demais:
    prioridade = sorted(
        pacientes,
        key=lambda x: (x[2] != "urgente", -x[1]) #prioriza os urgentes e ordena a idade do maior para o menor para garantir que os mais velhos venham na sequência da prioridade.
    )
  
    # TODO: Exiba a ordem de atendimento com título e vírgulas:
    nomes = [p[0] for p in prioridade]  # pega só o nome de cada paciente

    return print(f"Ordem de Atendimento: {', '.join(nomes)}")
 

# Entrada do número de pacientes
n = int(input("Informe a quantidade de pacientes: ").strip())
ordem_atendimento(n)  

