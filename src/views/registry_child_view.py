import os
from typing import Dict


class RegistryChildViews:
    def registry_child_view(self) -> Dict:
        self.__clear()

        print('Criação de Cadastro de Crianca \n\n')
        child = input('Determine o nome da crianca: ')
        mother = input('Determine o nome da mae: ')
        father = input('Determine o nome do pai: ')
        class_id = input('Determine o Id da Turma: ')

        return {
            "child": child,
            "mother": mother,
            "father": father,
            "class_id": class_id 
        }
    
    def registry_child_success(self, new_child: any) -> None:
        self.__clear()

        message = '''
            Crianca cadastrada com sucesso!
            * Infos:
                Id da Matricula: {}
                Nome da crianca: {}
                Id da Turma: {}
        '''.format(new_child.id, new_child.name, new_child.school_class.id)
        print(message)

    def registry_child_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao cadastrar a Crianca.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
