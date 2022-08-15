import os


class RegistryClassViews:
    def registry_class_page(self) -> str:
        self.__clear()

        print('Criação de Turma \n\n')
        teacher = input('Determine o nome da professora: ')

        return teacher

    def registry_class_success(self, new_school_class: any) -> None:
        self.__clear()

        message = '''
            Turma cadastrada com sucesso!
            * Infos:
                Id da Turma: {}
                Professora da Turma: {}
        '''.format(new_school_class.id, new_school_class.teacher)
        print(message)

    def registry_class_fail(self) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao cadastrar a Turma, confira os campos apresentados
        '''
        print(message)
    
    def __clear(self):
        os.system('cls||clear')