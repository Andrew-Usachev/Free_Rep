# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Specify the language for the test run",
    )
