from typing import Dict
from src.models.school_repository import school_enrollment
from src.models.entities.child import Child

class RegistryChildController:

    def registry(self, child_informations: Dict):
        try:
            class_registry = self.__get_school_class(child_informations["class_id"])
            new_child_id = self.__get_new_child_id()

            new_child = Child(
                new_child_id,
                child_informations["child"],
                child_informations["mother"],
                child_informations["father"],
                class_registry
            )
            school_enrollment.registry_child(new_child)
            
            return { "success": True, "child_registry": new_child }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __get_school_class(self, class_id: str) -> any:
        class_registry = school_enrollment.get_class(class_id)
        if class_registry is None: raise Exception('Falha ao cadastrar. Turma nao encontrada!')

        return class_registry

    def __get_new_child_id(self) -> str:
        children_count = school_enrollment.count_children()
        new_child_id = str(children_count + 1)
        return new_child_id
