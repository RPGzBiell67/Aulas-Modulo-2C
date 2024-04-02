class Aluno:
    def __init__(self, nome, data_nascimento, notas):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"

alunos = []

for _ in range(10):
    nome = input("Digite o nome do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
    notas = []
    for bimestre in range(1, 5):
        nota = float(input(f"Digite a nota do {bimestre}º bimestre: "))
        notas.append(nota)
    aluno = Aluno(nome, data_nascimento, notas)
    alunos.append(aluno)

print("\nResultados:")
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Data de Nascimento: {aluno.data_nascimento}")
    print("Notas:", aluno.notas)
    print("Média:", aluno.calcular_media())
    print("Situação:", aluno.verificar_aprovacao())
    print()