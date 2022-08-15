def introduction_page():
    message = '''
        Sistema de Cadastro Escolar

        * Cadastrar Turma - 1
        * Cadastrar Crianca - 2
        * Buscar Turma - 3
        * Buscar Crianca - 4
        * Sair - 5
    '''

    print(message)
    command = input('Comando: ')

    return command
