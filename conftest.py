import pytest as pytest
from pathlib import Path
from distutils.util import strtobool
from utils.params import Params


@pytest.fixture(scope="session")
def automation_manager():
    print("Creating automation manager")
    manager = AutomationManagement()
    return manager


class AutomationManagement:

    def __init__(self):
        self.project_dir = Path(__file__).parent

        self.test_parameters = Params("{}/{}".format(self.project_dir, "data/test_params.json"),
                                      "{}/{}".format(self.project_dir, "globals/env_params.json")).params

        self.browser_headless_mode = bool(strtobool(str(self.test_parameters['browser_headless_mode'])))