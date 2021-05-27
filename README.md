# python-pytest-ci


``` bash
# check tests
pytest

# with coverage
coverage run -m pytest

# check all python files with pylint 
find . -type f -name "*.py" | xargs pylint 
```