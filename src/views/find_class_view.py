import os
# o que a importação do "os" faz?

# classe para criar a turma
class FindSchoolClassViews:
    def find_class_view(self) -> str:
        self.__clear() ##  (?? )pq usou o método privado aqui?

        print('Busca de Registro de Turma \n\n')
        class_id = input('Determine o id da turma para busca: ')
        
        return class_id
    
    # criando a classe de cadastro da turma com sucesso
    def find_class_sucess(self, class_regstry: any) -> None:
        self.__clear()
    
        ## (??) isso é pra apagar o cache?? os registros (??)
 
        message = '''
            Turma {} - Professora {}
            * Infos:
        '''.format(
            class_registry["class_id"],
            class_registry["class_teacher"]
        )

        for registry in class_registry["registries"]:
            message += '''\n
                Id da Matricula: {}
                Nome da crianca: {}
                Mae da crianca: {}
                Pai da crianca: {}
            '''.format(
                registry["id"],
                registry["name"],
                registry["mother"],
                registry["father"]
            )

        print(message)

    def find_class_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao buscar Turma.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
