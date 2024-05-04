import os
import xml.etree.ElementTree as ET
from pretty_printer import *
from common import *


def generateReport(component):
    clearWarningsBuffer()
    clearErrorsBuffer()
    clearSummaryBuffer()

    try:
        # files = filter(os.path.isfile, os.listdir(os.curdir + f'/{component}/logs/junit'))
        files = os.listdir(os.curdir + f'/{component}/logs/junit')
    except:
        print()
        INFO(displayText='SUMMARY')
        SUMMARY(tests=0, failures=0)
        showSummaryBuffer()
        print()
        return

    # # Generate test report
    totalFailures = 0
    totalTests = 0
    # summaryMessage = ''

    # # warningsBuffer = []
    # # failuresBuffer = []
    for file in files:
        tree = ET.parse(f'./{component}/logs/junit/{file}')

        # Print warning if test case has no assertion
        for testCase in tree.iter('testcase'):
            if int(testCase.attrib['assertions']) == 0:
                file = relativePath(testCase.attrib['file'])
                WARNING(displayText=f"Test case {testCase.attrib['name']} in test group {testCase.attrib['classname']} has no assertions!", \
                        filename=file, line=testCase.attrib['line'])

        # Print failures
        for failure in tree.iter('failure'):
            message = failure.attrib['message'].replace('{newline}', '\\n')
            message = message.replace(r'\n', '\n')
            message = message.split(" ", 1)

            file = relativePath(message[0].split(':')[0])

            message[0] = os.path.split(message[0])
            line = message[0][1].split(':')[1]

            errorMessage = f'\n{message[1]}'

            errorMessage = errorMessage.replace('\n', ' '*len(str(file)))



            ERROR(displayText=errorMessage, filename=file, line=line)

        # Get information for summary
        testSuite = tree.getroot()

        testGroup = testSuite.attrib['name']
        failures = testSuite.attrib['failures']
        tests = testSuite.attrib['tests']

        totalFailures = totalFailures + int(failures)
        totalTests = totalTests + int(tests)

        SUMMARY(tests=int(tests), failures=int(failures), testGroup=testGroup)

    if warnings():
        print()
        showWarningsBuffer()

    if errors():
        print()
        showErrorsBuffer()

    if summary():
        print()
        INFO(displayText='SUMMARY')
        showSummaryBuffer()
        clearSummaryBuffer()

        print()
        SUMMARY(tests=int(totalTests), failures=int(totalFailures))
        showSummaryBuffer()
        print()
