from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='heimdall-bank-validate',
    version='1.0.0',
    url='https://github.com/thaisribeiro/heimdall',
    license='MIT License',
    author='Thais Ribeiro',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='thaisnribeiro2008@gmail.com',
    keywords='Bank Validate',
    description=u'Python implementation for bank account validation',
    packages=['heimdall_bank_validate'],
    install_requires=['setuptools','nose','isort','coverage','flake8','wheel','pytest-cov','pytest-runner','pytest'])
