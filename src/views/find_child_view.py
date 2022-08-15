import os

class FindChildViews:
    def find_child_view(self) -> str:
        self.__clear()

        print('Busca de Registro de Crianca \n\n')
        child_name = input('Determine o nome da crianca para busca: ')

        return child_name
    
    def find_child_success(self, child_registry: any) -> None:
        self.__clear()

        message = '''
            Matricula de Crianca
            * Infos:
                Id da Matricula: {}
                Nome da crianca: {}
                Mae da crianca: {}
                Pai da crianca: {}
                Id da Turma: {}
                Professora da turma: {}
        '''.format(
            child_registry["id"],
            child_registry["name"],
            child_registry["mother"],
            child_registry["father"],
            child_registry["class_id"],
            child_registry["class_teacher"]
        )
        print(message)
    
    def find_child_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao buscar matricula.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
