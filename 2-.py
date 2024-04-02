def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    alunos = []
    n_alunos = int(input("Digite o número de alunos na sala: "))

    for i in range(n_alunos):
        print(f"\nAluno {i+1}:")
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        notas = []
        for j in range(4):
            nota = float(input(f"Nota do {j+1}º bimestre: "))
            notas.append(nota)

        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)

        alunos.append({"Nome": nome, "Data de Nascimento": data_nascimento, "Notas": notas, "Média": media, "Situação": situacao})

    print("\nResultados:")
    for aluno in alunos:
        print("\nNome:", aluno["Nome"])
        print("Data de Nascimento:", aluno["Data de Nascimento"])
        print("Notas:", aluno["Notas"])
        print("Média:", aluno["Média"])
        print("Situação:", aluno["Situação"])

if __name__ == "__main__":
    main()
