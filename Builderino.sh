python3 -m venv venv
source ./venv/bin/activate
python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
