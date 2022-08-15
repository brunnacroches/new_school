from typing import Dict
from src.models.school_repository import school_enrollment

class FindSchoolClassController:

    def find(self, child_name: str):
        try:
            children_registries = self.__search_children_registries_by_class_id(child_name)
            registries = self.__format_registries_info(children_registries)
            return { "success": True, "registries": registries }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __search_children_registries_by_class_id(self, class_id: str) -> any:
        children_registries = school_enrollment.get_children_by_class_id(class_id)
        if children_registries == []: raise Exception('Turma vazia') ### (!!!!)

        return children_registries

    def __format_registries_info(self, children_registries: any):
        
        class_id = children_registries[0].school_class.id
        class_teacher = children_registries[0].school_class.teacher

        registries = []
        for child in children_registries:
            registries.append({
                "id": child.id,
                "name": child.name,
                "mother": child.mother,
                "father": child.father,
            })
        
        return {
            "class_id": class_id,
            "class_teacher": class_teacher,
            "registries": registries
        }
