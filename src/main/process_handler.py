# fica as princiais funções criadas na views
from .constructor.introduction_process import introduction_process
from .constructor.registry_class_process import registry_class_process
from .constructor.registry_child_process import registry_child_process
from .constructor.find_class_process import find_class_process
from .constructor.find_child_process import find_child_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': registry_class_process()
        elif command == '2': registry_child_process()
        elif command == '3': find_class_process()
        elif command == '4': find_child_process()
        elif command == '5': exit()
        else: print('\nComando nao encontrado, tente novamente!\n\n')

