# Função que calcula idade, com base no nascimento e ano atual:
def calcular_idade(ano_nascimento, ano_atual=2024):
    idade = ano_atual - ano_nascimento
    return idade
# Resultado do cálculo da indade:    
resultado = calcular_idade(1987)
print(f'Sua idade é {resultado}.')
# Função que calcula a bioimpedância, com base na massa e altura, tendo o cercentual de massa
# gorda fixo em 29%:
def calculo_bioimpedancia(massa_kg, altura_m):
    imc = massa_kg / (altura_m ** 2)
    total_massa_gorda = massa_kg * 29 / 100
    return imc, total_massa_gorda # Retorno da função.
# Criação das variáveis, para armazenar o resultado do cálculo da bioimpedância:
imc_calculado, massa_gorda = calculo_bioimpedancia(78, 1.75)
# Arredondamento do resultado:
imc_arredondado = round(imc_calculado, 2)

print(f'''Seu IMC é {imc_arredondado}kg/m² e
      seu total de gordura é {massa_gorda}''')