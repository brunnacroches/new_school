from src.views.registry_class_view import RegistryClassViews
from src.controllers.registry_class_controller import RegistryClassController

def registry_class_process() -> None:
    registry_class_view = RegistryClassViews()
    registry_class_controller = RegistryClassController()

    teacher = registry_class_view.registry_class_page()
    new_school_class = registry_class_controller.registry(teacher)

    if new_school_class is not None: registry_class_view.registry_class_success(new_school_class)
    else: registry_class_view.registry_class_fail()
