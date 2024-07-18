def calcular_idade(ano_nascimento, ano_atual=2024):
    idade = ano_atual - ano_nascimento
    return idade
    
resultado = calcular_idade(1987)
print(f'Sua idade é {resultado}.')

def calculo_bioimpedancia(massa_kg, altura_m):
    imc = massa_kg / (altura_m ** 2)
    total_massa_gorda = massa_kg * 29 / 100
    return imc, total_massa_gorda
imc_calculado, massa_gorda = calculo_bioimpedancia(78, 1.75)
imc_arredondado = round(imc_calculado, 2)

print(f'''Seu IMC é {imc_arredondado}kg/m² e
      seu total de gordura é {massa_gorda}''')