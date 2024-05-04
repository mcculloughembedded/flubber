import pytest
from pretty_printer import *

from ansi_colours import *

@pytest.fixture(autouse=True)
def setup_and_teardown(tmpdir):
    # Setup
    clearSummaryBuffer()

    yield # Run tests

    # Teardown

def test_passing(capsys):
    SUMMARY(tests=10, failures=0)
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"Total: {colourise('OK', colour.GREEN)}(10 tests ran)\n"

def test_failing(capsys):
    SUMMARY(tests=10, failures=5)
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"Total: {colourise('ERRORS', colour.RED)}(10 tests ran, 5 failures)\n"

def test_passing_alternative_test_group(capsys):
    SUMMARY(tests=10, failures=0, testGroup='dummyTestGroup')
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"dummyTestGroup: {colourise('OK', colour.GREEN)}(10 tests ran)\n"

def test_failing_alternative_test_group(capsys):
    SUMMARY(tests=10, failures=5, testGroup='dummyTestGroup')
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"dummyTestGroup: {colourise('ERRORS', colour.RED)}(10 tests ran, 5 failures)\n"

def test_no_tests(capsys):
    SUMMARY(tests=0, failures=0)
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"Total: {colourise('ERRORS', colour.RED)}(0 tests ran)\n"

def test_no_tests_alternative_test_group(capsys):
    SUMMARY(tests=0, failures=0, testGroup='dummyTestGroup')
    showSummaryBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"dummyTestGroup: {colourise('ERRORS', colour.RED)}(0 tests ran)\n"

def test_no_tests_non_zero_failures(capsys):
    with pytest.raises(ValueError, match='It is not possible to have run no tests and have failures!'):
        SUMMARY(tests=0, failures=5)

    with pytest.raises(ValueError, match='It is not possible to have run no tests and have failures!'):
        SUMMARY(tests=0, failures=5, testGroup='dummyTestGroup')

def test_more_failures_than_tests(capsys):
    with pytest.raises(ValueError, match='It is not possible to have more failures than tests!'):
        SUMMARY(tests=1, failures=5)

    with pytest.raises(ValueError, match='It is not possible to have more failures than tests!'):
        SUMMARY(tests=1, failures=5, testGroup='dummyTestGroup')

def test_print_buffer_is_used(capsys):
    SUMMARY(tests=10, failures=4)
    captured = capsys.readouterr()
    assert not captured.out
