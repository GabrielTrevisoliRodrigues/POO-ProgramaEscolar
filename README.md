# Sistema de Cadastro de Alunos, Professores, Disciplinas e Turmas

Este projeto implementa um **sistema de cadastro** para gerenciar **alunos**, **professores**, **disciplinas**, **turmas** e **atividades**. O sistema foi desenvolvido utilizando conceitos fundamentais de **Programação Orientada a Objetos (POO)** e segue as **boas práticas de programação**, incluindo os princípios **SOLID**.

## Funcionalidades

- Cadastro de alunos, professores, disciplinas e turmas.
- Gerenciamento de atividades associadas às turmas.
- Listagem de turmas, alunos e professores cadastrados.
- Edição e exclusão de registros.
- Persistência de dados das turmas em um arquivo JSON.

## Estrutura do Sistema

### Classes Principais

1. **Pessoa**: Classe base para representar uma pessoa, com atributos como nome e CPF.
2. **Aluno** e **Professor**: Herdam da classe `Pessoa`, representando os respectivos papéis no sistema.
3. **Atividade**: Representa uma atividade associada a uma turma.
4. **Disciplina**: Representa uma disciplina associada a um professor.
5. **Turma**: Gerencia alunos, atividades e disciplinas.
6. **Exibidor**: Responsável por exibir informações no console.
7. **Entrada**: Coleta dados do usuário.
8. **SistemaDeCadastro**: Gerencia o cadastro e as operações relacionadas às entidades do sistema.

### Estrutura do Código

- **Encapsulamento**: Cada classe encapsula seus atributos e métodos, garantindo que os dados sejam manipulados apenas por meio de métodos específicos.
- **Herança**: As classes `Aluno` e `Professor` herdam da classe base `Pessoa`, promovendo a reutilização de código.
- **Polimorfismo**: Permite tratar objetos das subclasses (`Aluno` e `Professor`) como objetos da classe base (`Pessoa`).
- **Composição**: Classes como `Turma` e `Disciplina` utilizam outras classes (`Aluno`, `Professor`, etc.) como atributos, promovendo modularidade.

## Princípios SOLID Aplicados

1. **SRP (Single Responsibility Principle)**: Cada classe tem uma única responsabilidade. Por exemplo:
   - `Pessoa` armazena e formata informações de uma pessoa.
   - `Exibidor` é responsável apenas por exibir informações no console.
   - `Entrada` coleta dados do usuário.
2. **OCP (Open/Closed Principle)**: As classes `Aluno` e `Professor` estendem a classe `Pessoa`, permitindo a adição de novas funcionalidades sem modificar a classe base.
3. **LSP (Liskov Substitution Principle)**: Objetos das subclasses (`Aluno` e `Professor`) podem substituir objetos da classe base (`Pessoa`) sem alterar o comportamento do programa.
4. **ISP (Interface Segregation Principle)**: As classes são projetadas para cumprir responsabilidades específicas, evitando interfaces grandes e genéricas.
5. **DIP (Dependency Inversion Principle)**: A função `main` depende de abstrações (`SistemaDeCadastro`) e não de implementações específicas, facilitando a manutenção e testes.

## Persistência de Dados

O sistema utiliza o módulo `json` para salvar e carregar os dados das turmas em um arquivo JSON, garantindo a persistência das informações.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
