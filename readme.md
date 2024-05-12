# Flubber

Flubber is a command line interface (CLI) that implements a number of helper functions for setting up and executing [CppUTest](https://cpputest.github.io/) tests.
Flubber aims to be easy to use and extensible.

Most users should be able to jump right in and focus on their tests.
Flubber's structure provides flexibility for those who want or need more control.

# Table of Contents
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Run Your First Test](./docs/first-test.md)
* [Test Components](./docs/test-components.md)
* [Command Reference](./docs/command-reference.md)
* [Compiler Flags](./docs/compiler-flags.md)

### Requirements

#### Windows
* [Git Bash for Windows](https://git-scm.com/downloads)
* [Podman](https://podman.io/)

#### Linux
* [Podman](https://podman.io/)

## Installation
1. Install the tools listed in the [Requirements](#Requirements) section.
2. Add this repository into the root of your project as a submodule.\
From your project's root:
    ````console
    git submodule add https://github.com/mcculloughembedded/flubber
    `````
3. Checkout a stable version.\
    From your project's root:
    ````console
    cd flubber
    git checkout <latest-tag>
    `````
4. Build the Podman image.\
    From `<project-root>/flubber/`:
    ````console
    podman build -t unit-tests -f dockerfile .
    `````

That's it!
The next step is to [run your first test](./docs/first-test.md).

## What's With the Name?
Flubber is named after Ned Brainard's invention from the movie [The Absent Minded Professor](https://en.wikipedia.org/wiki/The_Absent-Minded_Professor).
I watched the [remake](https://en.wikipedia.org/wiki/Flubber_(film)) when I was a child, and for some reason it stuck.
