from src.models.school_repository import school_enrollment
from src.models.entities.school_class import SchoolClass

class RegistryClassController:

    def registry(self, teacher: str):
        try:
            class_count = school_enrollment.count_classes()
            new_class_id = str(class_count + 1)

            new_school_class = SchoolClass(new_class_id, teacher)
            school_enrollment.registry_class(new_school_class)

            return new_school_class
        except:
            return None