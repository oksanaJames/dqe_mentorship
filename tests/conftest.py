import pytest
from src.oop.company import Company
from src.oop.engineer import Engineer
from pathlib import Path
from _pytest.main import Session
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import datetime


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


def send_email():
    run_time = datetime.datetime.now()
    subject = f"Pytest results for '{run_time}' run"
    sender_email = os.environ["EMAIL_USR"]
    sender_password = os.environ["EMAIL_PSSWD"]
    recipient_email = os.environ["EMAIL_RECIPIENT"]
    body = f"""
        <html>
          <body>
            <p>This is an email sent from Pytest run for '{run_time}'. Please verify test results report in attachments.</p>
          </body>
        </html>
        """
    file_to_attach = "report.html"

    with open(file_to_attach, "rb") as attachment:
        # Add the attachment to the message
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_to_attach}",
    )

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    html_part = MIMEText(body, "html")
    message.attach(html_part)
    message.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


@pytest.hookimpl()
def pytest_sessionfinish(session: Session, exitstatus):
    if exitstatus != 0:
        print("\nSending an email with results... ")
        send_email()
        print("\nEmail with results sent! ")

