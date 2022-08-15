from src.views.find_child_view import FindChildViews
from src.controllers.find_child_controller import FindChildController


def find_child_process() -> None:
    find_child_views = FindChildViews()
    find_child_controller = FindChildController()

    child_informations = find_child_views.find_child_view()
    response = find_child_controller.find(child_informations)

    if response["success"]: find_child_views.find_child_success(response["registry"])
    else: find_child_views.find_child_fail(response["error"])

