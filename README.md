# Python tests with GitHub Actions

This repository contains a sample implementation for testing Python code manual and automatic


## Optional requirement

If you don't want to install anything like Python, PyTest and PyLint, you can use the DevContainer which already contains all required tools. 

Steps to test: 
1. Clone this repository
1. Open folde locally in Visual Studio Code
1. Accept dialog to open this folder in a container again
1. Grab a tea or coffee until container is pulled completely

## Testing Manual

In VS Code Terminal just open bash: 

``` bash
# check tests
pytest

# check all python files with pylint 
find . -type f -name "*.py" | xargs pylint 
```

## Automatic with GitHub Actions

The folder `.github/workflows` contains the file [ci.yml](/.github/workflows/ci.yml) which is executed on GitHub everytime a push or a merge is requested for the Main-Branch. It will executed automatically before a push and merge into main. It fails if one step of the Pipeline fails. 
