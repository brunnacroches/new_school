from src.views.registry_child_view import RegistryChildViews
from src.controllers.registry_child_controller import RegistryChildController


def registry_child_process() -> None:
    registry_child_views = RegistryChildViews()
    registry_child_controller = RegistryChildController()

    child_informations = registry_child_views.registry_child_view()
    response = registry_child_controller.registry(child_informations)

    if response["success"]: registry_child_views.registry_child_success(response["child_registry"])
    else: registry_child_views.registry_child_fail(response["error"])

