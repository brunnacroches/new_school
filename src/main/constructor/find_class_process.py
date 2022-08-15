from src.views.find_class_view import FindSchoolClassViews
from src.controllers.find_class_controller import FindSchoolClassController


def find_class_process() -> None:
    find_class_views = FindSchoolClassViews()
    find_class_controller = FindSchoolClassController()

    child_informations = find_class_views.find_class_view()
    response = find_class_controller.find(child_informations)

    if response["success"]: find_class_views.find_class_success(response["registries"])
    else: find_class_views.find_class_fail(response["error"])

