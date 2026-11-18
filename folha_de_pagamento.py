import os

senha_feita = "123"
login_feito = "luiz"
tentativas = 0
max_tentativas = 3
acesso = False

def login_entrada(senha, login):
    return senha == senha_feita and login == login_feito

def calcular_inss(salario_base):
    if salario_base < 1621:
        return salario_base * 0.075
    elif salario_base <= 2902.84:
        return salario_base * 0.09
    elif salario_base <= 4354.27:
        return salario_base * 0.12
    else:
        return salario_base * 0.14

def calcular_irrf(salario_base, inss, dependentes):
    base = salario_base - inss - (dependentes * 189.59)
    if base <= 2428.80:
        aliquota = 0.0
        parcela_deduzir = 0.0
    elif base <= 2826.66:
        aliquota = 0.075
        parcela_deduzir = 182.16
    elif base <= 3751.05:
        aliquota = 0.15
        parcela_deduzir = 394.16
    elif base <= 4664.68:
        aliquota = 0.225
        parcela_deduzir = 675.49
    else:
        aliquota = 0.275
        parcela_deduzir = 908.73
    
    imposto = (base * aliquota) - parcela_deduzir
    return max(0.0, imposto)

def reducao(salario_base, imposto):
    if salario_base <= 5000:
        return 0.0
    elif salario_base <= 7350:
        desconto_reducao = 978.62 - (0.133145 * salario_base)
        imposto_final = imposto - desconto_reducao
        return max(0.0, imposto_final)
    else:
        return imposto

def calcular_vt(salario_base, vale_transporte):
    if vale_transporte == "S":
        return salario_base * 0.06
    return 0.0

def calcular_vr(valor_vr):
    if 500 <= valor_vr <= 800:
        return valor_vr * 0.20
    return 0.0

def calcular_plano_saude(dependentes):
    if dependentes == 0:
        return 150.0
    return 150.0 + (150.0 * dependentes)  # Titular + dependentes

def mostrar_contracheque(salario_base, inss, irrf, vt, vr, plano_saude):
    total_descontos = inss + irrf + vt + vr + plano_saude
    salario_liquido = salario_base - total_descontos
    
    os.system('cls')
    print('=' * 40)
    print('          CONTRACHEQUE MENSAL')
    print('=' * 40)
    print(f'Salário Base:        R$ {salario_base:10.2f}')
    print('-' * 40)
    print(f'(-) INSS:            R$ {inss:10.2f}')
    print(f'(-) IRRF:            R$ {irrf:10.2f}')
    print(f'(-) Vale Transporte: R$ {vt:10.2f}')
    print(f'(-) Vale Refeição:   R$ {vr:10.2f}')
    print(f'(-) Plano de Saúde:  R$ {plano_saude:10.2f}')
    print('-' * 40)
    print(f'Total de Descontos:  R$ {total_descontos:10.2f}')
    print(f'SALÁRIO LÍQUIDO:     R$ {salario_liquido:10.2f}')
    print('=' * 40)

# --- Execução do Programa ---
while tentativas < max_tentativas:
    os.system('cls')
    print('\n= Login Contracheque =')
    
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    
    acesso = login_entrada(senha, login)
    
    if acesso:
        print(f'\nBem-vindo, {login_feito}!')
        break
    else:
        tentativas += 1
        print(f'\nLogin ou senha incorretos! Tentativa {tentativas} de {max_tentativas}.')
        if tentativas < max_tentativas:
            input('Pressione Enter para tentar novamente...')

if not acesso:
    os.system('cls')
    print('\nMuitas tentativas feitas. Acesso bloqueado!')
    input('Pressione Enter para sair...')
    exit()

os.system('cls')
print('\n= Perguntas =')
salario_base = float(input('Digite seu salário base: ').replace(',', '.'))
vale_transporte = input('Gostaria de vale transporte (S/N): ').strip().upper()
vale_alimentacao = float(input('Quanto de vale refeição gostaria (500 a 800): ').replace(',', '.'))
dependentes = int(input('Quantos dependentes gostaria de colocar no plano de saúde: '))

inss = calcular_inss(salario_base)
irrf_bruto = calcular_irrf(salario_base, inss, dependentes)
irrf = reducao(salario_base, irrf_bruto)
vt = calcular_vt(salario_base, vale_transporte)
vr = calcular_vr(vale_alimentacao)
plano_saude = calcular_plano_saude(dependentes)

mostrar_contracheque(salario_base, inss, irrf, vt, vr, plano_saude)