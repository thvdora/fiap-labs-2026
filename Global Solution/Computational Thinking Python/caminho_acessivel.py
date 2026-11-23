# Estruturando dados para testar o algoritmo
locais = [
    "Estação Central - Elevador 1",
    "Estação Jardim Azul - Plataforma 2",
    "Terminal Vila Nova - Plataforma 3",
    "Estação Parque Sul - Entrada principal",
    "Rua das Acácias, 120",
    "Avenida Primavera, 450",
    "Rua dos Ipês, 85",
    "Avenida Central, 200",
    "Rua Bela Vista, 310",
    "Parque das Palmeiras - Entrada principal",
    "Praça da Harmonia - Coreto",
    "Parque Vila Verde - Banheiro acessível",
    "Praça do Sol - Área de lazer",
    "Biblioteca Municipal - Elevador",
    "Hospital Santa Clara - Entrada principal",
    "Escola Horizonte - Banheiro acessível",
    "Centro Comunitário Esperança - Entrada",
    "Rua das Flores, 150",
    "Avenida Brasil, 800",
    "Rua São Pedro, 65",
    "Avenida dos Estados, 1200",
    "Rua Monte Alegre, 90",
    "Praça da Independência - Ponto de ônibus"
]

problemas = [
    "Ausência de rampa",
    "Rampa danificada",
    "Calçada irregular",
    "Calçada bloqueada por obstáculos",
    "Elevador quebrado",
    "Escada sem alternativa acessível",
    "Ausência de piso tátil",
    "Piso tátil danificado",
    "Faixa de pedestres inadequada",
    "Banheiro inacessível",
    "Falta de iluminação pública",
    "Lixo acumulado na calçada",
    "Alagamento em via pública",
    "Buraco na calçada",
    "Buraco na via pública",
    "Ponto de ônibus sem acessibilidade",
    "Semáforo para pedestres danificado",
    "Ausência de faixa de pedestres",
    "Calçada estreita",
    "Árvore bloqueando a passagem",
    "Ausência de sinalização viária",
    "Pavimentação danificada"
]

gravidades = [
    "Alta",
    "Média",
    "Baixa"
]

classificacoes = {
    # --- Gravidade Alta ---
    "Ausência de rampa": "Alta",
    "Calçada bloqueada por obstáculos": "Alta",
    "Elevador quebrado": "Alta",
    "Escada sem alternativa acessível": "Alta",
    "Faixa de pedestres inadequada": "Alta",
    "Alagamento em via pública": "Alta",
    "Buraco na via pública": "Alta",
    "Semáforo para pedestres danificado": "Alta",
    "Ausência de faixa de pedestres": "Alta",
    "Árvore bloqueando a passagem": "Alta",
    "Ponto de ônibus sem acessibilidade": "Alta",

    # --- Gravidade Média ---
    "Falta de iluminação pública": "Média",
    "Rampa danificada": "Média",
    "Calçada irregular": "Média",
    "Ausência de piso tátil": "Média",
    "Banheiro inacessível": "Média",
    "Lixo acumulado na calçada": "Média",
    "Buraco na calçada": "Média",
    "Calçada estreita": "Média",
    "Pavimentação danificada": "Média",

    # --- Gravidade Baixa ---
    "Piso tátil danificado": "Baixa"
}

    # Categorias dos problemas

categorias = {
    "Acessibilidade": [
    "Ausência de rampa",
    "Rampa danificada",
    "Elevador quebrado",
    "Escada sem alternativa acessível",
    "Ausência de piso tátil",
    "Piso tátil danificado",
    "Banheiro inacessível",
    "Ponto de ônibus sem acessibilidade"
    ],

    "Mobilidade urbana": [
    "Calçada irregular",
    "Calçada bloqueada por obstáculos",
    "Faixa de pedestres inadequada",
    "Alagamento em via pública",
    "Buraco na via pública",
    "Semáforo para pedestres danificado",
    "Ausência de faixa de pedestres",
    "Calçada estreita",
    "Árvore bloqueando a passagem",
    ],

    "Infraestrutura urbana": [
    "Falta de iluminação pública",
    "Lixo acumulado na calçada",
    "Buraco na calçada",
    "Pavimentação danificada"
    ]
    }

# Permitir que o usuário registre problemas
registros = []

# Classifica a gravidade do problema com base no dicionário de classificações, se não estiver no dicionário, assume Média
def classificar_gravidade(problema):
    return classificacoes.get(problema, "Média")

def mostrar_ocorrencia(ocorrencia):
    print("\n=== PROBLEMA REGISTRADO ===")
    print(f"Local: {ocorrencia['local']}")
    print(f"Problema: {ocorrencia['problema']}")
    print(f"Gravidade: {ocorrencia['gravidade']}")

# Escolher local do problema
def escolher_local():
    print("\n=== LOCAIS CADASTRADOS ===")

    for i, local in enumerate(locais, start=1):
        print(f"{i} - {local}")

    print("0 - Outro local (digitar manualmente)")

    entrada = input("\nEscolha o número do local: ")

    # Validar a opção escolhida
    if not entrada.isdigit() or not 0 <= int(entrada) <= len(locais):
        print("\nOpção inválida!")
        return

    # Permitir digitar outro local
    if int(entrada) == 0:
        local = input("Digite a localização do problema: ")

        if not local:
            print("\nA localização não pode ficar vazia!")
            return

        return local

    else:
        return locais[int(entrada) - 1]

# Escolher gravidade do problema
def escolher_gravidade():
    print("\n=== GRAVIDADES ===")

    for i, gravidade in enumerate(gravidades, start=1):
        print(f"{i} - {gravidade}")

    entrada = input("\nEscolha o número da gravidade: ")

    # Validar a opção escolhida
    if not entrada.isdigit() or not 1 <= int(entrada) <= len(gravidades):
        print("\nOpção inválida!")
        return

    return gravidades[int(entrada) - 1]

# Permitir que o usuário registre problemas

# Permitir que o usuário registre problemas
def registrar_problema():

    # Escolher local do problema
    local = escolher_local()

    if not local:
        return

    # Mostrar menu numerado com os tipos de problemas
    print("\n=== TIPOS DE PROBLEMAS ===")

    for i, problema in enumerate(problemas, start=1):
        print(f"{i} - {problema}")

    print("0 - Outro problema (digitar manualmente)")

    entrada = input("\nEscolha o número do problema: ")

    # Validar a opção escolhida
    if not entrada.isdigit() or not 0 <= int(entrada) <= len(problemas):
        print("\nOpção inválida!")
        return

    # Permitir digitar outro problema
    if int(entrada) == 0:
        problema_escolhido = input("Digite o problema identificado: ")

        if not problema_escolhido.strip():
            print("\nO problema não pode ficar vazio!")
            return

    else:
        problema_escolhido = problemas[int(entrada) - 1]

    # Classificar gravidade automaticamente
    gravidade = classificar_gravidade(problema_escolhido)

    # Armazenar os dados no dicionário
    registros.append({
        "local": local,
        "problema": problema_escolhido,
        "gravidade": gravidade
    })

    print("\nProblema registrado com sucesso!")
    print(f"Local: {local}")
    print(f"Problema: {problema_escolhido}")
    print(f"Gravidade: {gravidade}")

# Consultando os problemas registrados:
def consultar_problemas():
    if not registros:
        print("\nNenhum problema registrado.")
    else:
        for ocorrencia in registros:
            mostrar_ocorrencia(ocorrencia)

# Buscando problemas por gravidade
def buscar_problemas_por_gravidade():
    gravidade = escolher_gravidade()

    if not gravidade:
        return

    encontrou = False

    for ocorrencia in registros:
        if ocorrencia["gravidade"] == gravidade:
            mostrar_ocorrencia(ocorrencia)
            encontrou = True

    if not encontrou:
        print(f"\nNenhum problema registrado com gravidade '{gravidade}'.")

def calcular_estatisticas():
    if not registros:
        print("\nNenhum problema registrado.")
        return

    total_registros = len(registros)
    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de registros: {total_registros}")

    # Contagem de problemas por gravidade
    total_alta = 0
    total_media = 0
    total_baixa = 0

    for ocorrencia in registros:
        if ocorrencia["gravidade"] == "Alta":
            total_alta += 1
        elif ocorrencia["gravidade"] == "Média":
            total_media += 1
        elif ocorrencia["gravidade"] == "Baixa":
            total_baixa += 1
    
    print("\n--- PROBLEMAS POR GRAVIDADE ---")
    print(f"Alta:  {total_alta}")
    print(f"Média: {total_media}")
    print(f"Baixa: {total_baixa}")
    print("--------------------------------")

    # Contagem de problemas por categoria
    print("\n--- PROBLEMAS POR CATEGORIA ---")

    for categoria, lista_problemas in categorias.items():
        total_categoria = 0

        for ocorrencia in registros:
            if ocorrencia["problema"] in lista_problemas:
                total_categoria += 1

        print(f"{categoria}: {total_categoria}")

    print("--------------------------------")

# MENU PRINCIPAL
def menu_principal():
    print("\n========== CAMINHO ACESSÍVEL ==========")
    print("1 - Registrar problema")
    print("2 - Consultar problemas registrados")
    print("3 - Filtrar problemas por gravidade")
    print("4 - Visualizar estatísticas")
    print("0 - Sair do sistema")
    print("=======================================")

# SISTEMA PRINCIPAL
def main():
    while True:
        inicio = input("\nDigite 10 para acessar o sistema ou 0 para sair: ")

        if inicio == "0":
            print("\nEncerrando o sistema...")
            break

        if inicio != "10":
            print("\nOpção inválida! Tente novamente.")
            continue

        while True:
            menu_principal()
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                registrar_problema()
            elif opcao == "2":
                consultar_problemas()
            elif opcao == "3":
                buscar_problemas_por_gravidade()
            elif opcao == "4":
                calcular_estatisticas()
            elif opcao == "0":
                break
            else:
                print("\nOpção inválida!")
                continue

            continuar = input("\nDeseja voltar ao menu? (S/N): ").upper()
            if continuar == "N":
                break

        print("\nVoltando à tela inicial...")

main()