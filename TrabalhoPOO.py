"""
Este programa implementa um sistema de cadastro para gerenciar alunos, professores, disciplinas, turmas e atividades.
Ele segue os princípios de programação orientada a objetos (POO) e boas práticas de design, como os princípios SOLID.
O sistema permite cadastrar, listar, editar e excluir entidades, além de salvar os dados das turmas em um arquivo JSON.
"""

import json  # Importa o módulo JSON para salvar e carregar dados em formato JSON

# Classe base para representar uma pessoa
# Princípio SRP (Single Responsibility Principle): 
# A classe Pessoa é responsável apenas por armazenar e formatar informações de uma pessoa.
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome  # Nome da pessoa
        self.cpf = cpf  # CPF da pessoa

    # Método para formatar as informações da pessoa
    def formatar_info(self, exibir_cpf=True):
        return f"Nome: {self.nome}, CPF: {self.cpf}" if exibir_cpf else f"Nome: {self.nome}"

    # Converte os dados da pessoa para um dicionário
    def to_dict(self):
        return {"tipo": self.__class__.__name__, "nome": self.nome, "cpf": self.cpf}

# Classe Aluno que herda de Pessoa
# Princípio OCP (Open/Closed Principle): 
# A classe Aluno estende a classe Pessoa, permitindo reutilizar o código sem modificar a classe base.
class Aluno(Pessoa):
    pass

# Classe Professor que herda de Pessoa
# Princípio OCP (Open/Closed Principle): 
# A classe Professor também estende Pessoa, seguindo o mesmo princípio de reutilização.
class Professor(Pessoa):
    pass

# Classe para representar uma atividade
# Princípio SRP: A classe Atividade é responsável apenas por armazenar informações de uma atividade.
class Atividade:
    def __init__(self, descricao):
        self.descricao = descricao  # Descrição da atividade

    # Converte os dados da atividade para um dicionário
    def to_dict(self):
        return {"descricao": self.descricao}

# Classe para representar uma disciplina
# Princípio SRP: A classe Disciplina é responsável apenas por armazenar informações de uma disciplina.
class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome  # Nome da disciplina
        self.professor = professor  # Professor responsável pela disciplina

    # Remove o professor da disciplina
    def remover_professor(self):
        self.professor = None

    # Converte os dados da disciplina para um dicionário
    def to_dict(self):
        return {
            "nome": self.nome,
            "professor": self.professor.to_dict() if self.professor else None,
        }

# Classe para representar uma turma
# Princípio SRP: A classe Turma é responsável apenas por gerenciar informações de uma turma.
class Turma:
    def __init__(self, nome, disciplina):
        self.nome = nome  # Nome da turma
        self.disciplina = disciplina  # Disciplina associada à turma
        self.alunos = []  # Lista de alunos na turma
        self.atividades = []  # Lista de atividades na turma

    # Adiciona um aluno à turma
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    # Remove um aluno da turma
    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    # Adiciona uma atividade à turma
    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    # Converte os dados da turma para um dicionário
    def to_dict(self):
        return {
            "nome": self.nome,
            "disciplina": self.disciplina.to_dict(),
            "alunos": [aluno.to_dict() for aluno in self.alunos],
            "atividades": [atv.to_dict() for atv in self.atividades]
        }

# Classe para exibir informações no console
# Princípio SRP: A classe Exibidor é responsável apenas por exibir informações no console.
class Exibidor:
    @staticmethod
    def exibir_pessoa(pessoa, exibir_cpf=True):
        print(pessoa.formatar_info(exibir_cpf))

    @staticmethod
    def exibir_disciplina(disciplina):
        print(f"Disciplina: {disciplina.nome}")
        if disciplina.professor:
            print("Professor responsável:")
            Exibidor.exibir_pessoa(disciplina.professor)
        else:
            print("Professor responsável: [sem professor]")

    @staticmethod
    def exibir_turma(turma):
        print(f"\nTurma: {turma.nome}")
        Exibidor.exibir_disciplina(turma.disciplina)
        print("Alunos:")
        for aluno in turma.alunos:
            Exibidor.exibir_pessoa(aluno, exibir_cpf=False)
        print("Atividades:")
        for atividade in turma.atividades:
            print(f" - {atividade.descricao}")
        print()

# Classe para entrada de dados do usuário
# Princípio SRP: A classe Entrada é responsável apenas por coletar dados do usuário.
class Entrada:
    @staticmethod
    def obter_dados_pessoa(tipo):
        nome = input(f"Nome do {tipo}: ")
        cpf = input(f"CPF do {tipo}: ")
        return nome, cpf

    @staticmethod
    def editar_pessoa(pessoa):
        novo_nome = input(f"Novo nome para {pessoa.nome} (pressione Enter para manter): ")
        novo_cpf = input(f"Novo CPF para {pessoa.nome} (pressione Enter para manter): ")
        if novo_nome:
            pessoa.nome = novo_nome
        if novo_cpf:
            pessoa.cpf = novo_cpf
        print("Dados atualizados com sucesso!")
        Exibidor.exibir_pessoa(pessoa)

# Classe principal para gerenciar o sistema de cadastro
# Princípio SRP e ISP (Interface Segregation Principle):
# A classe SistemaDeCadastro gerencia o cadastro e as operações relacionadas às entidades do sistema.
class SistemaDeCadastro:
    def __init__(self):
        self.alunos = []  # Lista de alunos cadastrados
        self.professores = []  # Lista de professores cadastrados
        self.disciplinas = []  # Lista de disciplinas cadastradas
        self.turmas = []  # Lista de turmas cadastradas

    # Métodos para cadastrar alunos, professores, disciplinas, turmas, etc.
    def cadastrar_aluno(self):
        nome, cpf = Entrada.obter_dados_pessoa("aluno")
        self.alunos.append(Aluno(nome, cpf))
        print("Aluno cadastrado com sucesso!\n")

    def cadastrar_professor(self):
        nome, cpf = Entrada.obter_dados_pessoa("professor")
        self.professores.append(Professor(nome, cpf))
        print("Professor cadastrado com sucesso!\n")

    def cadastrar_disciplina(self):
        if not self.professores:
            print("Cadastre um professor primeiro.\n")
            return
        nome = input("Nome da disciplina: ")
        print("Escolha o professor pelo índice:")
        for i, prof in enumerate(self.professores, 1):
            print(f"{i} - {prof.formatar_info()}")
        escolha = int(input()) - 1
        self.disciplinas.append(Disciplina(nome, self.professores[escolha]))
        print("Disciplina cadastrada com sucesso!\n")

    def cadastrar_turma(self):
        if not self.disciplinas:
            print("Cadastre uma disciplina primeiro.\n")
            return
        nome = input("Nome da turma: ")
        print("Escolha a disciplina pelo índice:")
        for i, disc in enumerate(self.disciplinas, 1):
            print(f"{i} - {disc.nome}")
        escolha = int(input()) - 1
        self.turmas.append(Turma(nome, self.disciplinas[escolha]))
        print("Turma cadastrada com sucesso!\n")

    # Outros métodos para gerenciar atividades, alunos em turmas, exclusões, etc.

    def salvar_turmas_json(self, nome_arquivo="turmas.json"):
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump([turma.to_dict() for turma in self.turmas], f, indent=2, ensure_ascii=False)
        print(f"Turmas salvas em '{nome_arquivo}'\n")

# Função principal que exibe o menu e gerencia as opções do sistema
# Princípio DIP (Dependency Inversion Principle):
# A função `main` depende de abstrações (SistemaDeCadastro) e não de implementações específicas.
def main():
    sistema = SistemaDeCadastro()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Disciplina")
        print("4. Cadastrar Turma")
        print("5. Cadastrar Atividade em Turma")
        print("6. Adicionar Aluno em Turma")
        print("7. Listar Turmas e Cadastros")
        print("8. Excluir Aluno")
        print("9. Excluir Professor")
        print("10. Editar Dados de Pessoa")
        print("11. Salvar dados das turmas em JSON")
        print("0. Sair\n")
        opcao = input("Escolha uma opção: ")
        print()
        if not opcao.isdigit():
            print("Opção inválida!")
            continue
        opcao = int(opcao)

        # Chama os métodos correspondentes com base na opção escolhida
        if opcao == 1:
            sistema.cadastrar_aluno()
        elif opcao == 2:
            sistema.cadastrar_professor()
        elif opcao == 3:
            sistema.cadastrar_disciplina()
        elif opcao == 4:
            sistema.cadastrar_turma()
        elif opcao == 5:
            sistema.cadastrar_atividade()
        elif opcao == 6:
            sistema.adicionar_aluno_na_turma()
        elif opcao == 7:
            sistema.listar_turmas()
        elif opcao == 8:
            sistema.excluir_aluno()
        elif opcao == 9:
            sistema.excluir_professor()
        elif opcao == 10:
            sistema.editar_dados_pessoa()
        elif opcao == 11:
            sistema.salvar_turmas_json()
        elif opcao == 0:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

# Executa o programa
if __name__ == "__main__":
    main()
