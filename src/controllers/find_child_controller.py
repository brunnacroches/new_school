from typing import Dict
from src.models.school_repository import school_enrollment

class FindChildController:

    def find(self, child_name: str):
        try:
            child_registry = self.__search_child_registry(child_name)
            registry = self.__format_registry_info(child_registry)
            return { "success": True, "registry": registry }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __search_child_registry(self, child_name: str) -> any:
        child_registry = school_enrollment.get_child(child_name)
        if child_registry is None: raise Exception('Crianca nao encontrada!')

        return child_registry

    def __format_registry_info(self, child_registry: any):
        return {
            "id": child_registry.id,
            "name": child_registry.name,
            "mother": child_registry.mother,
            "father": child_registry.father,
            "class_id": child_registry.school_class.id,
            "class_teacher": child_registry.school_class.teacher,
        }
