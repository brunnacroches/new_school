ESTRUTURA MVC
## DO PROJETO 01
Exercício N°1:
- Uma possui várias turmas. Cada turma é composta por algumas crianças e
uma professora. Além disso, cada criança é definida por uma matricula com registros de pai e mãe.
Para que haja maior controle das turmas, foi proposto um sistema que possui as seguintes
funcionalidades:
* Criar uma turma específica com uma professora
* Cadastrar uma criança e inseri-la em uma turma
* Buscar uma turma e apresentar todas as pessoas que a compõem
* Buscar uma criança e apresentar suas informações de matricula
Implemente tal sistema!
- Observações importantes!
* O projeto deve ser salvo e armazenado em um repositório no GitHub
* Não há necessidade da utilização de um banco de dados para tal, entretanto caso seja optado pela
utilização, deixe os arquivos necessários (.sql) no projeto
* O projeto deve possuir interação em console
* A escolha de tecnologia é totalmente livre – Pode-se utilizar qualquer tipo de ferramenta
presente
na linguagem Python. Além disso, pode-se utilizar qualquer tipo de paradigma desejado
(Programação Funcional, POO, Programação assincrona, Programação Procedural…)
- Sobre a avaliação:
* Serão tomados como elementos avaliativos todos os processos de construção do sistema:
Organização de Diretórios, Formação dos Commits, Formação dos PRs (caso haja), Criação e
formatação de métodos e funções, utilização correta de pacotes importados, nomeação de
variáveis…
OBS: O projeto tem como objetivo servir como um estudo de caso para entender melhor os
modos de produção e perspectiva pessoal sobre construção e arquitetura de projetos. Portanto,
não há “construção errada” e basta implementar o sistema de acordo com convicções
pessoais. É desejavel a conclusão do projeto, entretanto, em casos de dificuldade, basta apenas
indicar a resolução
Prazo: 4 dias úteis → Finalização 26/07 23:00 (Terça-feira dia 26 de maio as 23 horas)
- Caso a finalização seja realizada antes do prazo estipulado, basta entrar em contato


## DEFININDO AS AÇÕES DO PROJETO 
SISTEMA
PASSO 01 - Criar turma específica com uma professora
PASSO 02 - Cadastrar uma criança e inseri-la em uma turma
PASSO 03 - Buscar turma e apresentar todas as pessoas que a compõem
buscar uma criança e apresentar suas informações de matrícula

Resolução:
Quais são as tarefas bem definidas no projeto?
1 - Criar turma específica com uma professora
2 - Cadastar aluno
3 - Listar alunos cadastrados
4 - Buscar/Procurar criança e apresentar suas informações

Criando uma função para cada ~

subir no github


## PASSO 01
ESTRUTURA DO PROJETO 
- src
    - models 
    - main
    - views
    - controllers

## POR ONDE COMEÇAR > main
Na main tem o arquivo chamado process_handler
nele vai ser chamado todas funções que iniciam a 
chamada dos principais métodos da view

- ---> process_handler.py (src>main>process_handler>)

# 01 main > constructor
 - aqui faz a chamada para inicializar as funções
 que foram criadas dentro da views


## 02 views
 - Função cadastrar turma (find_class_view)
 - Função cadastrar a criança (find_child_view)
 - Função buscar turma
 - Função sair 