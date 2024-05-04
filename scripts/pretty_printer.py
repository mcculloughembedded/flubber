from ansi_colours import *

warningsBuffer = []
errorsBuffer = []
remarksBuffer = []
summaryBuffer = []

def clearSummaryBuffer():
    summaryBuffer[:] = []

def showSummaryBuffer():
    for line in summaryBuffer:
        print(line)

def getSummaryLineLength(lineNumber: int):
    return len(summaryBuffer[lineNumber])

def summary():
    return bool(summaryBuffer)

def clearRemarksBuffer():
    remarksBuffer[:] = []

def showRemarksBuffer():
    for line in remarksBuffer:
        print(line)

def remarks():
    return bool(remarksBuffer)

def clearErrorsBuffer():
    errorsBuffer[:] = []

def showErrorsBuffer():
    for line in errorsBuffer:
        print(line)

def errors():
    return bool(errorsBuffer)

def clearWarningsBuffer():
    warningsBuffer[:] = []

def showWarningsBuffer():
    for line in warningsBuffer:
        print(line)

def warnings():
    return bool(warningsBuffer)

def HEADING(displayText: str):
    print(f"{colourise(f'{displayText}', colour.GREEN)}")

def INFO(displayText: str):
    print(f"{colourise(f'{displayText}', colour.CYAN)}")

def REMARK(displayText: str, filename: str = None, line: int = None):
    if all([filename, line]):
        remarksBuffer.append(f"{filename}:{line} {colourise('remark', colour.PURPLE)}: {displayText}")
    else:
        if filename is not None or line is not None:
            raise ValueError('File and line must be specified together.')

        remarksBuffer.append(f"{colourise('remark', colour.PURPLE)}: {displayText}")

def ERROR(displayText: str, filename: str = None, line: int = None):
    if all([filename, line]):
        errorsBuffer.append(f"{filename}:{line} {colourise(f'error: {displayText}', colour.RED)}")
    else:
        if filename is not None or line is not None:
            raise ValueError('File and line must be specified together.')

        errorsBuffer.append(f"{colourise(f'error: {displayText}', colour.RED)}")

def WARNING(displayText: str, filename: str = None, line: int = None):
    if all([filename, line]):
        warningsBuffer.append(f"{filename}:{line} {colourise('warning', colour.BLUE)}: {displayText}")
    else:
        if filename is not None or line is not None:
            raise ValueError('File and line must be specified together.')

        warningsBuffer.append(f"{colourise('warning', colour.BLUE)}: {displayText}")

def SUMMARY(tests: int, failures: int, testGroup: str = 'Total'):
    status = colourise('OK', colour.GREEN)
    failureReport = ''

    if failures != 0:
        status = colourise('ERRORS', colour.RED)
        failureReport = f', {failures} failures'

    if tests == 0:
        if failures != 0:
            raise ValueError('It is not possible to have run no tests and have failures!')
        status = colourise('ERRORS', colour.RED)

    if failures > tests:
        raise ValueError('It is not possible to have more failures than tests!')

    message = f'{testGroup}: {status}({tests} tests ran{failureReport})'
    summaryBuffer.append(message)
