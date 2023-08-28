import pytest
from src.oop.company import Company
from src.oop.engineer import Engineer
from pathlib import Path
from _pytest.main import Session
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter


FAILURE_FILE = Path() / "failures.txt"

@pytest.fixture
def supply_url():
    return "https://reqres.in/api"


@pytest.fixture
def define_company():
    return Company('Fruits', address='Ocean street, 1')


@pytest.fixture
def define_employee():
    return Engineer('Johnny Cash', 55)


@pytest.hookimpl()
def pytest_sessionstart(session: Session):
    if FAILURE_FILE.exists():
        # Delete the file if it already exists
        FAILURE_FILE.unlink()
    FAILURE_FILE.touch()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # All code prior to yield statement would be ran prior
    # to any other of the same fixtures defined

    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        try:  # Just to not crash py.test reporting
            with open(str(FAILURE_FILE), "a") as f:
                f.write(result.nodeid + "\n")
        except Exception as e:
            print("ERROR", e)
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter: TerminalReporter, exitstatus: int, config):
    yield
    print(f"Failures outputted to: {FAILURE_FILE}")


@pytest.fixture(scope='function')
def get_test_name(request):
    import sys
    sys.stderr.write('\n' + request.node.name + ' starts!')

    def get_test_name_finish():
        print('\n' + request.node.name + ' finished!')
    request.addfinalizer(get_test_name_finish)
    return request.fixturename


def pytest_html_report_title(report):
    report.title = "Pytest Unit Tests report!"


