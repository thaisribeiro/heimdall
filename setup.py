import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heimdall",
    version="0.0.1",
    author="Thais Ribeiro // Bruna Balestê",
    author_email="thais.ribeiro@luizalabs.com",
    description="Validador de Dados Bancários",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thaisribeiro/Heimdall",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)