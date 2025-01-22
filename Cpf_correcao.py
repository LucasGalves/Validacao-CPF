def pontuandoCPF(str_cpf):

    cpf = ""

    for i in range(len(str_cpf)):
        if (0 < i < 9) and (i % 3 == 0):
            cpf = cpf + "."
        elif i == 9:
            cpf = cpf + "-"
        cpf = cpf + f"{str_cpf[i]}"

    return cpf
        


def verifica(cpf):
    cpf_temp = []

    # Criando cpf temporário:
    for i in range(9):
        cpf_temp.append(int(cpf[i]))

    # Primeiro Digito de Validação:
    cpf_temp.append(validacao(cpf_temp))

    # Segundo Digito de Validação:
    cpf_temp.append(validacao(cpf_temp))

    # Arrumando para comparar:
    for i in range(len(cpf_temp)):
        cpf_temp[i] = str(cpf_temp[i])

    # --- Check:
    print("\n")
    if cpf == cpf_temp:
        print("CPF está correto!")
    else:
        print(f"Cpf inválido!\n   Tente algo como: {pontuandoCPF(cpf_temp)}") # Exibe com os verificadores corretos
        testando1(cpf) # Exibe possibilidades com os verificadores originais
        testando2(cpf) # Exibe possibilidades trocando os digitos entre si

    print("\n")


def validacao(cpf):
    x = 10
    soma = 0
    validador = 0

    # Se não possui digito validador (ex: 123.456.789-__)
    if len(cpf) == 9:
        a1, a2 = 0, 9
    # Se possui 1 digito validador   (ex: 123.456.789-1_)
    else:
        a1, a2 = 1, 10

    # Calculo:
    for i in range(a1, a2):
        digito = int(cpf[i]) * x
        soma = soma + digito
        x = x - 1
        # esse calculo é feito assim: 
        # (primeiro digito * 10) + (segundo digito * 9) + (terceiro digito * 8) + (...

    resto = soma % 11
    if resto > 1:
        validador = 11 - resto
    elif resto <= 1:
        validador = 0

    # Retorna um único digito validador:
    return validador


def copiarCPF(original):
    copia = []
    for i in range(len(original) - 2):
        original[i] = int(original[i])
        copia.append(original[i])

    return copia


def testando1(cpf):
    cpf = list(cpf)
    cpf_temporario = []

    # Pegar os numeros verificadores originais
    # Exemplo: 123.456.789-XY
    cpf_check1 = int(cpf[-2]) # cpf_check1 = X
    cpf_check2 = int(cpf[-1]) # cpf_check2 = Y

    
    for i in range(len(cpf)-2): # Para cada digito
        for ii in range(10): # Para cada possibilidade
            cpf_temporario = copiarCPF(cpf)

            cpf_temporario[i] = ii
            
            cpf_temporario.append(validacao(cpf_temporario))
            cpf_temporario.append(validacao(cpf_temporario))
            if cpf_temporario[-2] == cpf_check1 and cpf_temporario[-1] == cpf_check2:
                print(f"                Ou: {pontuandoCPF(cpf_temporario)}")


def testando2(cpf):
    cpf = list(cpf)
    cpf_temporario = []

    # Pegar os numeros verificadores originais
    # Exemplo: 123.456.789-XY
    cpf_check1 = int(cpf[-2]) # cpf_check1 = X
    cpf_check2 = int(cpf[-1]) # cpf_check2 = Y


    for i in range(len(cpf)-3):
        cpf_temporario = copiarCPF(cpf)

        temp = cpf_temporario[i]
        cpf_temporario[i] = cpf_temporario[i+1]
        cpf_temporario[i+1] = temp
            
        cpf_temporario.append(validacao(cpf_temporario))
        cpf_temporario.append(validacao(cpf_temporario))
        if cpf_temporario[-2] == cpf_check1 and cpf_temporario[-1] == cpf_check2:
            print(f"                Ou: {pontuandoCPF(cpf_temporario)}")

# -------------------------- Main -------------------------- #
def main():
    cpf = ""

    while True:
        cpf = input("Digite seu CPF => ")

        # Padroniza o input
        cpf = cpf.replace(".", "").replace(",", "").replace("-", "").replace(" ", "")

        if len(cpf) == 11:
            try:
                verifica(list(cpf))
            except:
                print("CPF ERRO! Tente novamente\n")

        else:
            print("CPF ERRO! Tente novamente\n")


#=======================================================================================#
print("|##### Verificador de CPF [versao 3.3] #####|")
print("|-> Programa feito por Lucas Galves Simoes  |\n")
main()
