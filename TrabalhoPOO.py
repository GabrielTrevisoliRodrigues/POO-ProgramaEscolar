
import json

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def formatar_info(self, exibir_cpf=True):
        return f"Nome: {self.nome}, CPF: {self.cpf}" if exibir_cpf else f"Nome: {self.nome}"

    def to_dict(self):
        return {"tipo": self.__class__.__name__, "nome": self.nome, "cpf": self.cpf}

class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass

class Atividade:
    def __init__(self, descricao):
        self.descricao = descricao

    def to_dict(self):
        return {"descricao": self.descricao}

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def remover_professor(self):
        self.professor = None

    def to_dict(self):
        return {
            "nome": self.nome,
            "professor": self.professor.to_dict() if self.professor else None,
        }

class Turma:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.alunos = []
        self.atividades = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def to_dict(self):
        return {
            "nome": self.nome,
            "disciplina": self.disciplina.to_dict(),
            "alunos": [aluno.to_dict() for aluno in self.alunos],
            "atividades": [atv.to_dict() for atv in self.atividades]
        }

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

class SistemaDeCadastro:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.turmas = []

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

    def cadastrar_atividade(self):
        if not self.turmas:
            print("Cadastre uma turma primeiro.\n")
            return
        descricao = input("Descrição da atividade: ")
        print("Escolha a turma pelo índice:")
        for i, turma in enumerate(self.turmas, 1):
            print(f"{i} - {turma.nome}")
        escolha = int(input()) - 1
        self.turmas[escolha].adicionar_atividade(Atividade(descricao))
        print("Atividade adicionada com sucesso!\n")

    def adicionar_aluno_na_turma(self):
        if not self.alunos:
            print("Cadastre um aluno primeiro.\n")
            return
        if not self.turmas:
            print("Cadastre uma turma primeiro.\n")
            return
        print("Escolha o aluno pelo índice:")
        for i, aluno in enumerate(self.alunos, 1):
            print(f"{i} - {aluno.formatar_info(False)}")
        escolha_aluno = int(input()) - 1

        print("Escolha a turma pelo índice:")
        for i, turma in enumerate(self.turmas, 1):
            print(f"{i} - {turma.nome}")
        escolha_turma = int(input()) - 1

        self.turmas[escolha_turma].adicionar_aluno(self.alunos[escolha_aluno])
        print("Aluno adicionado à turma com sucesso!\n")

    def listar_turmas(self):
        if not self.turmas:
            print("Nenhuma turma cadastrada.\n")
            return
        for turma in self.turmas:
            Exibidor.exibir_turma(turma)

        print("=== Cadastros no sistema ===")
        for aluno in self.alunos:
            Exibidor.exibir_pessoa(aluno)
        for professor in self.professores:
            Exibidor.exibir_pessoa(professor)
        print()

    def excluir_aluno(self):
        if not self.alunos:
            print("Não há alunos cadastrados.\n")
            return
        print("Escolha o aluno para excluir:")
        for i, aluno in enumerate(self.alunos, 1):
            print(f"{i} - {aluno.formatar_info(False)}")
        escolha = int(input()) - 1
        removido = self.alunos.pop(escolha)
        for turma in self.turmas:
            turma.remover_aluno(removido)
        print("Aluno excluído:")
        Exibidor.exibir_pessoa(removido)
        print()

    def excluir_professor(self):
        if not self.professores:
            print("Não há professores cadastrados.\n")
            return
        print("Escolha o professor para excluir:")
        for i, prof in enumerate(self.professores, 1):
            print(f"{i} - {prof.formatar_info()}")
        escolha = int(input()) - 1
        removido = self.professores.pop(escolha)
        for disciplina in self.disciplinas:
            if disciplina.professor == removido:
                disciplina.remover_professor()
        print("Professor excluído:")
        Exibidor.exibir_pessoa(removido)
        print()

    def editar_dados_pessoa(self):
        print("Editar: 1 - Aluno | 2 - Professor")
        tipo = input("Escolha o tipo de pessoa: ")
        if tipo == "1":
            if not self.alunos:
                print("Não há alunos cadastrados.\n")
                return
            for i, aluno in enumerate(self.alunos, 1):
                print(f"{i} - {aluno.formatar_info(False)}")
            idx = int(input("Escolha o aluno: ")) - 1
            Entrada.editar_pessoa(self.alunos[idx])
        elif tipo == "2":
            if not self.professores:
                print("Não há professores cadastrados.\n")
                return
            for i, prof in enumerate(self.professores, 1):
                print(f"{i} - {prof.formatar_info()}")
            idx = int(input("Escolha o professor: ")) - 1
            Entrada.editar_pessoa(self.professores[idx])
        else:
            print("Opção inválida.\n")

    def salvar_turmas_json(self, nome_arquivo="turmas.json"):
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump([turma.to_dict() for turma in self.turmas], f, indent=2, ensure_ascii=False)
        print(f"Turmas salvas em '{nome_arquivo}'\n")

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

if __name__ == "__main__":
    main()
