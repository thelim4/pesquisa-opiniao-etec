
TOTAL_ENTREVISTADOS = 50

excelente = 0
bom = 0
ruim = 0

for i in range(TOTAL_ENTREVISTADOS):
    print("\nEntrevistado", i + 1)

    nome = input("Digite o nome: ")

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            print("Digite uma idade maior que zero.")
        except ValueError:
            print("Digite uma idade valida.")

    print("Opiniao sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    while True:
        try:
            opiniao = int(input("Digite 1, 2 ou 3: "))
            if opiniao in [1, 2, 3]:
                break
            print("Opcao invalida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas 1, 2 ou 3.")

    if opiniao == 1:
        excelente += 1
        resposta = "EXCELENTE"
    elif opiniao == 2:
        bom += 1
        resposta = "BOM"
    else:
        ruim += 1
        resposta = "RUIM"

    print("Resposta registrada para", nome + ":", resposta)

print("\n===== RESULTADO DA PESQUISA =====")
print("Total de entrevistados:", TOTAL_ENTREVISTADOS)
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas BOM:", bom)
print("Quantidade de respostas RUIM:", ruim)
