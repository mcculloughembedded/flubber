from typing import List, Optional

import typer
from typing_extensions import Annotated
import os
import subprocess
import sys

from clean import cleanDir
from pretty_printer import *
from compiler_output_printer import printCompilerOutput
from report_printer import generateReport

app = typer.Typer(add_completion=False,
                  help="""
                    Flubber Help
                  """)

reservedDirs = ['mocks', 'scripts']


def getValidComponents(components):
    clearWarningsBuffer()
    clearErrorsBuffer()
    # This handles the case where nothing is specified after --components=
    if components[0] == '':
        ERROR(displayText='No components specified.')
        showErrorsBuffer()
        return []

    # Generate set of all directories in the current directory, that does not
    # include the directories in reservedDirs
    possibleComponents = set(filter(os.path.isdir, os.listdir(
        f'../unit-tests/{os.curdir}'))) - set(reservedDirs)

    # Must convert to set to do efficient intersection
    testComponents = set(components)

    # Default is 'all', meaning all possible test components should be returned
    if list(testComponents)[0] == 'all':
        testComponents = possibleComponents
    # Filter out all test components that were not specified in the --components switch
    else:
        # Look for components in the list that are not in the list of potential components
        invalidComponents = list(testComponents - possibleComponents)
        if invalidComponents:
            # Only print a warning if the component does not exist
            # No need to terminate
            for component in invalidComponents:
                WARNING(
                    f'Test component {component} does not exist. Continuing...')

        testComponents = list(possibleComponents.intersection(testComponents))

    showWarningsBuffer()
    return testComponents


def confirm_existence_of_source_files(component):
    clearErrorsBuffer()
    with open(component + '/Makefile') as file:
        for line in file:
            if line.startswith('$(PROJECT_DIR)'):
                line = line.removeprefix('$(PROJECT_DIR)/')
                line = line.rstrip().removesuffix('\\').rstrip()

                path = f'../{line}'
                if not os.path.exists(path):
                    ERROR(
                        displayText=f"{line} not found! Check the filepaths in this component's Makefile.")

    showErrorsBuffer()


@app.command()
def run(components: Annotated[
    Optional[List[str]],
    typer.Option(help='Comma separated list of test components')] = ['all'],
):
    """
    Build and run a test component

    Use --components= to specify individual components
    """
    for component in getValidComponents(str.split(components[0], ',')):
        heading = f'Running test component {component}'
        print('-'*len(heading))
        HEADING(heading)
        print('-'*len(heading))

        confirm_existence_of_source_files(component)

        sys.stdout.flush()
        subprocess.run(['../unit-test-executor/scripts/run.sh', component])

        # printCompilerOutput(component)
        # generateReport(component)


@app.command()
def clean(components: Annotated[
    Optional[List[str]],
    typer.Option(help='Comma separated list of test components')] = ['all']
):
    """
    Remove all build artifacts from a test component

    Use --components= to specify individual components
    """
    for component in getValidComponents(str.split(components[0], ',')):
        INFO(f'Cleaning test component {component}')
        cleanDir(component)


@app.command()
def new_component(name: Annotated[
    Optional[List[str]],
    typer.Option(help='The name of the component to create')] = ['all']
):
    """
    Create a new component with a given name

    Use --name= to specify the name
    """
    sys.stdout.flush()
    subprocess.run(['../unit-test-executor/scripts/new-component.sh', name[0]])


if __name__ == "__main__":
    app()
