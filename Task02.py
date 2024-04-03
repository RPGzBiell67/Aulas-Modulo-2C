firstInt = int(input("Digite o primeiro numero inteiro: "))
secondInt = int(input("Digite o segundo numero inteiro: "))
thirdReal = float(input("Digite o numero real: "))

product = (firstInt * 2) * (secondInt / 2)
soma = (firstInt * 3) + thirdReal
cube = thirdReal ** 3

print("Valores e Calculos:")
print(f"Produto do dobro do primeiro com metade do segundo: {product}")
print(f"A soma do triplo do primeiro com o terceiro: {soma}")
print(f"O terceiro elevado ao cubo: {cube}")


height = float(input("Insira a altura da pessoa (em metros): "))

ideal_weight = (72.7 * height) - 58

print(f"O peso ideal para uma pessoa de {height:.2f} metros é: {ideal_weight:.2f} kg.")


gender = input("Digite seu gênero (M para masculino ou F para feminino): ").strip().upper()
height = float(input("Digite sua altura em metros: "))

if gender == "M":
    ideal_weight = (72.7 * height) - 58
elif gender == "F":
    ideal_weight = (62.1 * height) - 44.7
else:
    ideal_weight = "Gênero inválido"

print(f"O peso ideal para uma pessoa do seu sexo e altura é: {ideal_weight} kg.")


peso = float(input("Informe o peso do peixe pescado pelo João (em kg): "))

if peso <= 50:
    excesso = 0
    multa = 0
else:
    excesso = peso - 50
    multa = excesso * 4

print(f"Peso do peixe: {peso} kg")
if excesso == 0:
    print("Nenhum excesso.")
else:
    print(f"Excesso: {excesso} kg")
if multa == 0:
    print("Não está bem.")
else:
    print(f"Multa R$ {multa:.2f}")


    hourly_wage = float(input("Insira seu salário por hora em R$"))
hours_worked = float(input("Insira o número de horas trabalhadas por mês"))

salary_bruto = hourly_wage * hours_worked

ir = salary_bruto * 0.11
inss = salary_bruto * 0.08
sindicato = salary_bruto * 0.05

salary_liquido = salary_bruto - ir - inss - sindicato

print(f"\n=== Salário ===")
print(f"Salário Bruto: R$ {salary_bruto:.2f}")
print(f"- IR (11%): R$ {ir:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"= Salário Líquido: R$ {salary_liquido:.2f}")


area_size = float(input("Informe o tamanho da área a ser pintada (em m²): "))

liters_of_paint_required = (area_size / 3)

number_of_tins_required = liters_of_paint_required // 18

remaining_paint = liters_of_paint_required % 18

cost_of_tins = number_of_tins_required * 80

print(f"=== Pintura necessária ===")
print(f"- A área a ser pintada: {area_size} m²")
print(f"- A quantidade de tinta necessária: {liters_of_paint_required:.2f} litros")
print(f"- O número de latas necessárias: {number_of_tins_required}")
print(f"- O custo das latas: R$ {cost_of_tins:.2f}")
if remaining_paint > 0:
    print(f"- A quantidade restante de tinta: {remaining_paint:.2f} litros")


    area_to_be_painted = float(input("Informe a área a ser pintada (em m²):"))

coverage = 6
liters_required = (area_to_be_painted / coverage) + (area_to_be_painted / 100 * 10)

tins_required = liters_required // 18
cost_tins = tins_required * 80

galons_required = (liters_required // 3.6) + (liters_required % 3.6 > 0)
cost_galons = galons_required * 25

mixed_cost = (liters_required // 18) * 80 + (liters_required % 18) * 25

print(f"=== Pintura necessária ===")
print(f"- Obrigatório: {liters_required:.2f} Litros")
print(f"- Comprando apenas latas de 18 litros: {tins_required} latas (R$ {cost_tins:.2f})")
print(f"- Comprando apenas galões de 3,6 litros: {galons_required} galões (R$ {cost_galons:.2f})")
print(f"- Uma mistura de latas e galões: {tins_required + (liters_required % 18) > 0} latas e {(liters_required % 18) / 3.6:.2f} galões (R$ {mixed_cost:.2f})")


file_size = float(input("Digite o tamanho do arquivo a ser baixado (em MB): "))

link_speed = float(input("Insira a velocidade do link (em Mbps): "))

time_in_minutes = (file_size / link_speed) * 60

print(f"=== Tempo de download ===")
print(f"- O tamanho do arquivo: {file_size} MB")
print(f"- A velocidade da ligação: {link_speed} Mbps")
print(f"- O tempo de download: {time_in_minutes:.2f} minutos")